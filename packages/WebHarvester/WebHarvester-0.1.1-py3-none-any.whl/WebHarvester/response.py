import asyncio
from typing import Any, Dict, Optional
import aiohttp
import parsel
import json


class Response:
    def __init__(self, status: int, message: str, request: 'Request',
                 response: Optional[aiohttp.ClientResponse]):
        """
        初始化AsyncResponse实例。

        Args:
            status (int): 响应的HTTP状态码。
            message (str): 响应的状态消息。
            request (AsyncRequest): 请求对象。
            response (Optional[aiohttp.ClientResponse]): aiohttp的响应对象。
        """
        self.status_code = status
        self.message = message
        self.request = request
        self._response = response

    @property
    def status(self) -> int:
        """
        获取响应的HTTP状态码。

        Returns:
            int: HTTP状态码。
        """
        return self.status_code

    @property
    def reason(self) -> str:
        """
        获取响应的状态消息。

        Returns:
            str: 响应的状态消息。
        """
        return self.message

    @property
    def headers(self) -> Dict[str, str]:
        """
        获取响应头信息。

        Returns:
            Dict[str, str]: 响应头信息。
        """
        return dict(self._response.headers) if self._response else {}

    @property
    def cookies(self) -> Dict[str, str]:
        """
        获取响应Cookies。

        Returns:
            Dict[str, str]: 响应Cookies。
        """
        return {k: v.value for k, v in self._response.cookies.items()} if self._response else {}

    @property
    def elapsed(self) -> float:
        """
        获取请求的响应时间。

        Returns:
            float: 响应时间（秒）。
        """
        if self._response and hasattr(self._response, 'elapsed'):
            return self._response.elapsed.total_seconds()
        return 0.0

    async def text(self) -> str:
        """
        获取响应的文本内容。

        Returns:
            str: 响应的文本内容。
        """
        if self._response:
            for attempt in range(3):
                try:
                    return await self._response.text()
                except aiohttp.ClientError as e:
                    print(f"Attempt {attempt + 1} failed with error: aiohttp.ClientError {e}")
                    await asyncio.sleep(1)
            return f"Failed to retrieve text after {3} attempts."
        return ""

    async def content(self) -> bytes:
        """
        获取响应的二进制内容。

        Returns:
            bytes: 响应的二进制内容。
        """
        if self._response:
            try:
                return await self._response.read()
            except aiohttp.ClientError:
                return b""
        return b""

    async def json(self) -> Any:
        """
        获取响应的JSON内容。

        Returns:
            Any: 响应的JSON内容。
        """
        if self._response:
            try:
                return await self._response.json()
            except (aiohttp.ClientError, json.JSONDecodeError):
                return {}
        return {}

    async def parser(self) -> parsel.Selector:
        """
        将响应内容解析为parsel.Selector对象。

        Returns:
            parsel.Selector: 用于解析HTML的Selector对象。
        """
        return parsel.Selector(await self.text())
