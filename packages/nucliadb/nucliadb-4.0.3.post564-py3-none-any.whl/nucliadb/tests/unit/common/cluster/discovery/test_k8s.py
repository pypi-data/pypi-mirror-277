# Copyright (C) 2021 Bosutech XXI S.L.
#
# nucliadb is offered under the AGPL v3.0 and as commercial software.
# For commercial licensing, contact us at info@nuclia.com.
#
# AGPL:
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
import asyncio
import time
from unittest.mock import ANY, AsyncMock, MagicMock, patch

import kubernetes_asyncio.client.models.v1_container_status  # type: ignore
import kubernetes_asyncio.client.models.v1_object_meta  # type: ignore
import kubernetes_asyncio.client.models.v1_pod  # type: ignore
import kubernetes_asyncio.client.models.v1_pod_status  # type: ignore
import pytest

from nucliadb.common.cluster import manager
from nucliadb.common.cluster.discovery.k8s import EventType, KubernetesDiscovery
from nucliadb.common.cluster.discovery.types import IndexNodeMetadata
from nucliadb.common.cluster.settings import Settings
from nucliadb_protos import nodewriter_pb2

pytestmark = pytest.mark.asyncio


@pytest.fixture()
def writer_stub():
    writer_stub = MagicMock()
    writer_stub.GetMetadata = AsyncMock(
        return_value=nodewriter_pb2.NodeMetadata(
            node_id="node_id", shard_count=1, available_disk=10, total_disk=10
        )
    )
    with (
        patch(
            "nucliadb.common.cluster.discovery.base.nodewriter_pb2_grpc.NodeWriterStub",
            return_value=writer_stub,
        ),
        patch(
            "nucliadb.common.cluster.discovery.base.replication_pb2_grpc.ReplicationServiceStub",
            return_value=writer_stub,
        ),
        patch("nucliadb.common.cluster.discovery.base.get_traced_grpc_channel"),
    ):
        yield writer_stub


@pytest.fixture()
def k8s_discovery(writer_stub):
    disc = KubernetesDiscovery(Settings())
    disc.node_heartbeat_interval = 0.1
    manager.INDEX_NODES.clear()
    yield disc
    manager.INDEX_NODES.clear()


def create_k8s_event(
    type_: str = "ADDED",
    name: str = "node-0",
    container_name="reader",
    ready: bool = True,
) -> EventType:
    return {
        "type": type_,
        "object": kubernetes_asyncio.client.models.v1_pod.V1Pod(
            status=kubernetes_asyncio.client.models.v1_pod_status.V1PodStatus(
                container_statuses=[
                    kubernetes_asyncio.client.models.v1_container_status.V1ContainerStatus(
                        name=container_name,
                        ready=ready,
                        image="image",
                        image_id="image_id",
                        restart_count=0,
                    )
                ],
                pod_ip="1.2.3.4",
            ),
            metadata=kubernetes_asyncio.client.models.v1_object_meta.V1ObjectMeta(
                name=name, labels={"readReplica": "false"}
            ),
        ),
    }


async def test_get_node_metadata(k8s_discovery: KubernetesDiscovery, writer_stub):
    assert await k8s_discovery.get_node_metadata(
        "node-0", "1.1.1.1", read_replica=False
    ) == IndexNodeMetadata(
        node_id="node_id",
        shard_count=1,
        name="node_id",
        address="1.1.1.1",
        updated_at=ANY,
        available_disk=10,
    )

    writer_stub.GetMetadata.assert_awaited_once()

    # should be cached now
    await k8s_discovery.get_node_metadata("node-0", "1.1.1.1", read_replica=False)

    assert len(writer_stub.GetMetadata.mock_calls) == 1


async def test_update_node(k8s_discovery: KubernetesDiscovery):
    await k8s_discovery.update_node(create_k8s_event())
    assert len(manager.INDEX_NODES) == 1

    # update again
    await k8s_discovery.update_node(create_k8s_event())
    assert len(manager.INDEX_NODES) == 1


async def test_remove_node(k8s_discovery: KubernetesDiscovery):
    await k8s_discovery.update_node(create_k8s_event())

    assert len(manager.INDEX_NODES) == 1

    await k8s_discovery.update_node(create_k8s_event(ready=False))

    assert len(manager.INDEX_NODES) == 0


async def test_update_node_data_cache(k8s_discovery: KubernetesDiscovery, writer_stub):
    await k8s_discovery.update_node(create_k8s_event())

    task = asyncio.create_task(k8s_discovery.update_node_data_cache())

    await asyncio.sleep(k8s_discovery.node_heartbeat_interval + 0.1)

    task.cancel()

    assert len(writer_stub.GetMetadata.mock_calls) == 2


async def test_remove_stale_nodes(k8s_discovery: KubernetesDiscovery):
    manager.add_index_node(
        id="node_id",
        address="1.1.1.1",
        shard_count=1,
        available_disk=100,
    )
    nmd = IndexNodeMetadata(
        node_id="node_id",
        shard_count=1,
        available_disk=100,
        name="node_id",
        address="1.1.1.1",
        updated_at=time.time() - k8s_discovery.node_heartbeat_interval * 3,
    )
    k8s_discovery.node_id_cache["node_id"] = nmd

    assert len(k8s_discovery.node_id_cache) == 1
    assert len(manager.get_index_nodes()) == 1

    k8s_discovery._maybe_remove_stale_node("node_id")

    assert len(k8s_discovery.node_id_cache) == 0
    assert len(manager.get_index_nodes()) == 0
