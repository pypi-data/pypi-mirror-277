# vvclient - http

from typing import Any, Dict, Union, List

from aiohttp import ClientSession

from .errors import NotFoundError, HTTPException
from .types import AudioQueryType


class Route:
    def __init__(self, method: str, path: str) -> None:
        self.method = method
        self.path = path

    def create_uri(self, base_url: str) -> str:
        return base_url + self.path


class HTTPClient:
    def __init__(self, base_uri: str) -> None:
        self._base_uri = base_uri
        self._session = ClientSession()

    async def request(self, route: Route, **kwargs) -> Any:
        response = await self._session.request(
            route.method, route.create_uri(self._base_uri), **kwargs
        )
        if response.status == 200:
            if response.headers["Content-Type"] == "application/json":
                return await response.json()
            else:
                return await response.read()
        elif response.status == 204:
            return await response.read()
        elif response.status == 404:
            raise NotFoundError("Not found")
        else:
            raise HTTPException(await response.text(), response.status)

    async def close(self) -> None:
        await self._session.close()

    async def create_audio_query(
        self, params: Dict[str, Union[str, int]]
    ) -> AudioQueryType:
        return await self.request(Route("POST", "/audio_query"), params=params)

    async def synthesis(
        self, params: Dict[str, Union[str, int]], audio_query: AudioQueryType
    ) -> bytes:
        return await self.request(
            Route("POST", "/synthesis"), params=params, json=audio_query
        )

    async def engine_version(self) -> str:
        return await self.request(Route("GET", "/version"))

    async def core_versions(self) -> List[str]:
        return await self.request(Route("GET", "/core_versions"))

    async def initialize_speaker(self, params: Dict[str, Union[str, int]]) -> None:
        return await self.request(Route("POST", "/initialize_speaker"), params=params)

    async def is_initialized_speaker(self, params: Dict[str, Union[str, int]]) -> bool:
        return await self.request(Route("GET", "/is_initialized_speaker"), params=params)
