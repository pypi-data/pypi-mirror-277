# -*- coding: utf-8 -*-

import grpc.aio

from esdbclient.common import AsyncGrpcStreamers, SyncGrpcStreamers
from esdbclient.connection_spec import ConnectionSpec
from esdbclient.gossip import AsyncGossipService, GossipService
from esdbclient.persistent import (
    AsyncPersistentSubscriptionsService,
    PersistentSubscriptionsService,
)
from esdbclient.projections import AsyncProjectionsService, ProjectionsService
from esdbclient.streams import AsyncStreamsService, StreamsService


class ESDBConnection:
    def __init__(
        self,
        grpc_channel: grpc.Channel,
        grpc_target: str,
        connection_spec: ConnectionSpec,
    ) -> None:
        self._grpc_channel = grpc_channel
        self._grpc_target = grpc_target
        self._grpc_streamers = SyncGrpcStreamers()
        self.streams = StreamsService(
            grpc_channel=grpc_channel,
            connection_spec=connection_spec,
            grpc_streamers=self._grpc_streamers,
        )
        self.persistent_subscriptions = PersistentSubscriptionsService(
            channel=grpc_channel,
            connection_spec=connection_spec,
            grpc_streamers=self._grpc_streamers,
        )
        self.gossip = GossipService(
            channel=grpc_channel,
            connection_spec=connection_spec,
            grpc_streamers=self._grpc_streamers,
        )
        # self.cluster_gossip = ClusterGossipService(
        #     channel=grpc_channel,
        #     connection_spec=connection_spec,
        #     grpc_streamers=self._grpc_streamers,
        # )
        # self._channel_connectivity_state: Optional[ChannelConnectivity] = None
        # self.grpc_channel.subscribe(self._receive_channel_connectivity_state)
        self.projections = ProjectionsService(
            channel=grpc_channel,
            connection_spec=connection_spec,
            grpc_streamers=self._grpc_streamers,
        )

    @property
    def grpc_target(self) -> str:
        return self._grpc_target

    # def _receive_channel_connectivity_state(
    #     self, connectivity: ChannelConnectivity
    # ) -> None:
    #     self._channel_connectivity_state = connectivity
    #     # print("Channel connectivity state:", connectivity)

    def close(self) -> None:
        self._grpc_streamers.close()
        # self.grpc_channel.unsubscribe(self._receive_channel_connectivity_state)
        # sleep(0.1)  # Allow connectivity polling to stop.
        # print("closing channel")
        self._grpc_channel.close()
        # print("closed channel")


class AsyncioESDBConnection:
    def __init__(
        self,
        grpc_channel: grpc.aio.Channel,
        grpc_target: str,
        connection_spec: ConnectionSpec,
    ) -> None:
        self._grpc_channel = grpc_channel
        self._grpc_target = grpc_target
        self._grpc_streamers = AsyncGrpcStreamers()
        self.streams = AsyncStreamsService(
            grpc_channel,
            connection_spec=connection_spec,
            grpc_streamers=self._grpc_streamers,
        )
        self.persistent_subscriptions = AsyncPersistentSubscriptionsService(
            grpc_channel,
            connection_spec=connection_spec,
            grpc_streamers=self._grpc_streamers,
        )
        self.gossip = AsyncGossipService(
            grpc_channel,
            connection_spec=connection_spec,
            grpc_streamers=self._grpc_streamers,
        )
        self.projections = AsyncProjectionsService(
            grpc_channel,
            connection_spec=connection_spec,
            grpc_streamers=self._grpc_streamers,
        )

    @property
    def grpc_target(self) -> str:
        return self._grpc_target

    async def close(self) -> None:
        await self._grpc_streamers.close()
        await self._grpc_channel.close(grace=5)
