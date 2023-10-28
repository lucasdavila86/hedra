import asyncio
import time
import uuid
from typing import (
    Dict, 
    Coroutine, 
    Any,
    Union,
    List,
    Iterator
)
from hedra.core_rewrite.engines.client.client_types.common.base_client import BaseClient
from hedra.core.engines.types.common.ssl import get_default_ssl_context
from hedra.core.engines.types.common.timeouts import Timeouts
from .connection import UDPConnection
from .action import UDPAction
from .result import UDPResult
from .pool import Pool


class UDPClient(BaseClient[UDPAction, UDPResult]):

    __slots__ = (
        'mutations',
        'actions',
        'next_name',
        'initialized',
        'suspend',
        'session_id',
        'timeouts',
        '_hosts',
        'closed',
        'sem',
        'pool',
        'active',
        'waiter',
        'ssl_context'
    )

    def __init__(self, concurrency: int=10**3, timeouts: Timeouts = Timeouts(), reset_connections: bool=False) -> None:
        super(
            UDPClient,
            self
        ).__init__()

        self.session_id = str(uuid.uuid4())
        self.timeouts = timeouts
        
        self.next_name: Union[str, None] = None
        self.initialized: bool = False
        self.suspend: bool = False

        self.registered: Dict[str, UDPConnection] = {}
        self._hosts = {}
        self.closed = False

        self.sem = asyncio.Semaphore(value=concurrency)
        self.pool = Pool(concurrency, reset_connections=reset_connections)
        self.pool.create_pool()
        self.active = 0
        self.waiter = None

        self.ssl_context = get_default_ssl_context()

    def config_to_dict(self):
        return {
            'concurrency': self.pool.size,
            'timeouts': {
                'connect_timeout': self.timeouts.connect_timeout,
                'socket_read_timeout': self.timeouts.socket_read_timeout,
                'total_timeout': self.timeouts.total_timeout
            },
            'reset_connections': self.pool.reset_connections
        }
    
    async def receive(
        self,
        url: str, 
        user: str = None,
        tags: List[Dict[str, str]] = []
    ):

        request = UDPAction(
            self.next_name,
            url,
            wait_for_response=True,
            data=None,
            user=user,
            tags=tags             
        )

        if self.suspend and self.waiter is None:
            self.waiter = asyncio.Future()
            await self.waiter

            return request

        return await self.request(request)

    async def send(
        self,
        url: str, 
        wait_for_resonse: bool = False,
        data: Union[dict, str, bytes, Iterator] = None,
        user: str = None,
        tags: List[Dict[str, str]] = []
    ):

        request = UDPAction(
            self.next_name,
            url,
            wait_for_response=wait_for_resonse,
            data=data,
            user=user,
            tags=tags           
        )

        if self.suspend and self.waiter is None:
            self.waiter = asyncio.Future()
            await self.waiter

            return request

        return await self.request(request)

    async def prepare(self, action: UDPAction) -> Coroutine[Any, Any, None]:
        try:
            if action.url.is_ssl:
                action.ssl_context = self.ssl_context

            if self._hosts.get(action.url.hostname) is None:

                    socket_configs = await asyncio.wait_for(action.url.lookup(), timeout=self.timeouts.connect_timeout)
              
                    for ip_addr, configs in socket_configs.items():
                        for config in configs:

                            connection = UDPConnection()
                            
                            try:
                                await connection.make_connection(
                                    ip_addr,
                                    action.url.port,
                                    config,
                                    timeout=self.timeouts.connect_timeout
                                )

                                action.url.socket_config = config
                                action.url.ip_addr = ip_addr
                                action.url.has_ip_addr = True
                                break

                            except Exception as e: 
                                pass

                        if action.url.socket_config:
                            break

                    if action.url.socket_config is None:
                        raise Exception('Err. - No socket found.')
                    
                    self._hosts[action.url.hostname] = {
                        'ip_addr': action.url.ip_addr,
                        'socket_config': action.url.socket_config
                    }

            else:
                host_config = self._hosts[action.url.hostname]
                action.url.ip_addr = host_config.get('ip_addr')
                action.url.socket_config = host_config.get('socket_config')

            if action.is_setup is False:
                action.setup()

            self.registered[action.name] = action

        except Exception as e:   
            raise e

    async def request(self, action: UDPAction) -> Coroutine[Any, Any, UDPResult]:
 
        response = UDPResult(action)
        response.wait_start = time.monotonic()
        self.active += 1
 
        async with self.sem:
            connection = self.pool.connections.pop()
            
            try:

                if action.hooks.listen:
                    event = asyncio.Event()
                    action.hooks.channel_events.append(event)
                    await event.wait()

                if action.hooks.before:
                    action = await self.execute_before(action)
                    action.setup()

                response.start = time.monotonic()

                await connection.make_connection(
                    action.url.ip_addr,
                    action.url.port,
                    action.url.socket_config,
                    timeout=self.timeouts.connect_timeout
                )

                response.connect_end = time.monotonic()
                
                if action.encoded_data:
                    if action.is_stream:
                        action.write_chunks(connection)

                    else:
                        connection.write(action.encoded_data)

                response.write_end = time.monotonic()
                
                if action.wait_for_response:
                    response.body = await connection.readuntil()
         
                response.complete = time.monotonic()

                self.pool.connections.append(connection)

                if action.hooks.after:
                    response = await self.execute_after(action, response)
                    action.setup()

                if action.hooks.notify:
                    await asyncio.gather(*[
                        asyncio.create_task(
                            channel.call(response, action.hooks.listeners)
                        ) for channel in action.hooks.channels
                    ])

                    for listener in action.hooks.listeners: 
                        if len(listener.hooks.channel_events) > 0:
                            listener.setup()
                            event = listener.hooks.channel_events.pop()
                            if not event.is_set():
                                event.set()    

            except Exception as e:
                response.complete = time.monotonic()
                response.error = str(e)

                self.pool.connections.append(UDPConnection(reset_connection=self.pool.reset_connections))

            self.active -= 1
            if self.waiter and self.active <= self.pool.size:

                try:
                    self.waiter.set_result(None)
                    self.waiter = None

                except asyncio.InvalidStateError:
                    self.waiter = None

            return response

    async def close(self):
        if self.closed is False:
            await self.pool.close()
            self.closed = True
