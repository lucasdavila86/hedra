import asyncio
from types import FunctionType
from typing import Any, Dict, List
from hedra.core.engines.client.config import Config
from hedra.core.engines.types.graphql import (
    MercuryGraphQLClient,
    GraphQLAction
)
from hedra.core.engines.types.common.types import RequestTypes
from hedra.core.engines.types.common import Timeouts
from hedra.core.engines.client.store import ActionsStore
from .base_client import BaseClient


class GraphQLClient(BaseClient):

    def __init__(self, config: Config) -> None:
        super().__init__()
        
        self.session = MercuryGraphQLClient(
            concurrency=config.batch_size,
            timeouts=Timeouts(
                total_timeout=config.request_timeout
            ),
            reset_connections=config.reset_connections
        )
        self.request_type = RequestTypes.GRAPHQL
        self.actions: ActionsStore = None
        self.next_name = None
        self.intercept = False
        self.waiter = None

    def __getitem__(self, key: str):
        return self.session.registered.get(key)

    async def query(
        self,
        url: str, 
        query: str,
        operation_name: str = None,
        variables: Dict[str, Any] = None, 
        headers: Dict[str, str] = {}, 
        user: str = None, 
        tags: List[Dict[str, str]] = [],
        redirects: int = 10
    ):

        request = GraphQLAction(
            self.next_name,
            url,
            method='POST',
            headers=headers,
            data={
                "query": query,
                "operation_name": operation_name,
                "variables": variables
            },
            user=user,
            tags=tags,
            redirects=redirects
        )

        await self.session.prepare(request)

        if self.intercept:
            self.actions.store(self.next_name, request, self.session)
            
            loop = asyncio.get_event_loop()
            self.waiter = loop.create_future()
            await self.waiter

        return self.session
        
