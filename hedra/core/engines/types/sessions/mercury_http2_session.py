from mercury_http.http2 import MercuryHTTP2Client
from mercury_http.common.timeouts import Timeouts


class MercuryHTTP2Session:

    def __init__(self, pool_size=None, request_timeout=None, hard_cache=False, reset_connections: bool=False) -> None:
        self._connection_pool_size = pool_size
        self.request_timeout = request_timeout
        self.hard_cache = hard_cache
        self._reset_connections = reset_connections

    async def create(self) -> MercuryHTTP2Client:

        if self.request_timeout is None:
            self.request_timeout = 60
        
        timeouts = Timeouts(connect_timeout=5, total_timeout=self.request_timeout)

        return MercuryHTTP2Client(
            concurrency=self._connection_pool_size,
            timeouts=timeouts,
            hard_cache=self.hard_cache,
            reset_connections=self._reset_connections
        )
        
