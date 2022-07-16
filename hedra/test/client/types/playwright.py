
import inspect
from types import FunctionType
from typing import Any, Dict, List
from hedra.core.engines.types.playwright.client import MercuryPlaywrightClient
from hedra.core.engines.types.playwright import (
    Command,
    Page,
    URL,
    Input,
    Options
)
from hedra.core.engines.types.common.types import RequestTypes


class PlaywrightClient:

    def __init__(self, session: MercuryPlaywrightClient) -> None:
        self.session = session
        self.request_type = RequestTypes.PLAYWRIGHT
        self.next_name = None

    def __getitem__(self, key: str):
        return self.session.registered.get(key)

    async def run(
        self,
        command: str,
        selector: str=None,
        attribute: str=None,
        x_coordinate: int=0,
        y_coordinate: int=0,
        frame: int=0,
        location: str=None,
        headers: Dict[str, str]={},
        key: str=None,
        text: str=None,
        function: str=None,
        args: List[Any]=None,
        filepath: str=None,
        file: bytes=None,
        event: str=None,
        option: str=None,
        is_checked: bool=False,
        timeout: int=60000,
        extra: Dict[str, Any]={},
        switch_by: str='url',
        user: str=None,
        tags: List[Dict[str, str]]=[],
        checks: List[FunctionType] = []
    ):
        if self.session.registered.get(self.next_name) is None:
            result = await self.session.prepare(
                Command(
                    self.next_name,
                    command,
                    page=Page(
                        selector=selector,
                        attribute=attribute,
                        x_coordinate=x_coordinate,
                        y_coordinate=y_coordinate,
                        frame=frame
                    ),
                    url=URL(
                        location=location,
                        headers=headers
                    ),
                    input=Input(
                        key=key,
                        text=text,
                        function=function,
                        args=args,
                        filepath=filepath,
                        file=file
                    ),
                    options=Options(
                        event=event,
                        option=option,
                        is_checked=is_checked,
                        timeout=timeout,
                        extra=extra,
                        switch_by=switch_by
                    ),
                    user=user,
                    tags=tags,
                    checks=checks
                )
            )

            if isinstance(result, Exception):
                raise result