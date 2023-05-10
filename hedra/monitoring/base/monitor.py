import asyncio
import functools
import psutil
import signal
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from typing import (
    Dict, 
    List, 
    Union,
    Any
)


def handle_loop_stop(
    signame,
    loop: Union[asyncio.AbstractEventLoop, None],
    running_monitors: Dict[str, bool],
    monitors: Dict[str, asyncio.Future],
    executor: ThreadPoolExecutor
):
    try:

        for monitor_name in running_monitors:
            running_monitors[monitor_name] = False
            monitors[monitor_name].cancel()

        executor.shutdown()
        
        if loop:
            loop.close()

    except BrokenPipeError as e:
        executor.shutdown()
        raise e

    except RuntimeError as e:
        executor.shutdown()
        raise e

    except Exception as e:
        executor.shutdown()
        raise e


class BaseMonitor:

    def __init__(self) -> None:
        self.active: Dict[str, List[int]] = defaultdict(list)
        self.collected: Dict[str, List[int]] = defaultdict(list)
        self.cpu_count = psutil.cpu_count()
        self.stage_metrics: Dict[str, List[Union[int, float]]] = {}
        self.visibility_filters: Dict[str, bool] = defaultdict(lambda: False)
        self.stage_type: Union[Any, None] = None

        self._background_monitors: Dict[str, asyncio.Task] = {}
        self._sync_background_monitors: Dict[str, asyncio.Future] = {}
        self._running_monitors: Dict[str, bool] = {}

        self._loop: Union[asyncio.AbstractEventLoop, None] = None
        self._executor: Union[ThreadPoolExecutor, None] = None

    def start_background_monitor_sync(
        self,
        monitor_name: str,
        interval_sec: Union[int, float]=1
    ):
        if self._executor is None:
            self._executor = ThreadPoolExecutor(
                max_workers=psutil.cpu_count(logical=False)
            )

            for signame in ('SIGINT', 'SIGTERM', 'SIG_IGN'):
                signal_type: signal = getattr(signal, signame)

                signal.signal(
                    signal_type, 
                    lambda signame: handle_loop_stop(
                        signame,
                        self._loop,
                        self._running_monitors,
                        self._sync_background_monitors,
                        self._executor
                    )
                )
        
        self._sync_background_monitors[monitor_name] = self._executor.submit(
            functools.partial(
                self._monitor_at_interval,
                monitor_name,
                interval_sec=interval_sec
            )
        )

    async def start_background_monitor(
        self,
        monitor_name: str,
        interval_sec: Union[int, float]=1
    ):
        if self._loop is None:
            self._loop = asyncio.get_event_loop()

        if self._executor is None:
            self._executor = ThreadPoolExecutor(
                max_workers=psutil.cpu_count(logical=False)
            )

            for signame in ('SIGINT', 'SIGTERM', 'SIG_IGN'):
                self._loop.add_signal_handler(
                    getattr(signal, signame),
                    lambda signame=signame: handle_loop_stop(
                        signame,
                        self._loop,
                        self._running_monitors,
                        self._background_monitors,
                        self._executor
                    )
                )

        self._background_monitors[monitor_name] = self._loop.run_in_executor(
            self._executor,
            functools.partial(
                self._monitor_at_interval,
                monitor_name,
                interval_sec=interval_sec
            )
        )

    def update_monitor(str, monitor_name: str) -> Union[int, float]:
        raise NotImplementedError('Monitor background update method must be implemented in non-base Monitor class.')

    def store_monitor(self, monitor_name: str):
        self.collected[monitor_name] = list(self.active[monitor_name])
        del self.active[monitor_name]

    def trim_monitor_samples(
        self,
        monitor_name: str,
        trim_length: int
    ):
        if self.collected.get(monitor_name):
            self.collected[monitor_name][:trim_length]
        
    async def _update_background_monitor(
        self,
        monitor_name: str,
        interval_sec: Union[int, float]=1
    ):
        while self._running_monitors.get(monitor_name):
            await asyncio.sleep(interval_sec)
            self.update_monitor(monitor_name)

    def _monitor_at_interval(
        self, 
        monitor_name: str,
        interval_sec: Union[int, float]=1
    ):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        self._running_monitors[monitor_name] = True

        loop.run_until_complete(
            self._update_background_monitor(
                monitor_name,
                interval_sec=interval_sec
            )
        )

    def stop_background_monitor_sync(
        self,
        monitor_name: str
    ):
        
        self._running_monitors[monitor_name] = False
        self._sync_background_monitors[monitor_name].result()

        if self.active.get(monitor_name):
            self.collected[monitor_name].extend(
                list(self.active[monitor_name])
            )

    async def stop_background_monitor(
        self,
        monitor_name: str
    ):
        self._running_monitors[monitor_name] = False

        await self._background_monitors[monitor_name]

        if self.active.get(monitor_name):
            self.collected[monitor_name].extend(
                list(self.active[monitor_name])
            )

    def stop_all_background_monitors_sync(self):

        for monitor_name in self._running_monitors.keys():
            self._running_monitors[monitor_name] = False

        for monitor in self._sync_background_monitors.values():
            monitor.result()

        for monitor_name in self._running_monitors.keys():
            self.collected[monitor_name] = list(self.active[monitor_name])

    async def stop_all_background_monitors(self):

        for monitor_name in self._running_monitors.keys():
            self._running_monitors[monitor_name] = False

        await asyncio.gather(list(self._background_monitors.values()))

        for monitor_name in self._running_monitors.keys():
            self.collected[monitor_name] = list(self.active[monitor_name])

    def close(self):
        if self._executor:
            self._executor.shutdown()