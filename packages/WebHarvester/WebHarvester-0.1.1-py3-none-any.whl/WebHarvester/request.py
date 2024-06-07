import asyncio
from typing import Any, Dict, Optional

import aiohttp

from . import settings
from .response import Response
from .counter import Counter
from .logger_ex import LoggerEx


class Request:
    def __init__(self, retries: int = settings.RETRIES, retry_delay: int = settings.REQUEST_TIMEOUT,
                 timeout: int = settings.REQUEST_TIMEOUT, proxy: Optional[str] = None):
        """
        初始化AsyncRequest实例。

        Args:
            retries (int): 请求失败后的重试次数。
            retry_delay (int): 重试之间的等待时间（秒）。
            timeout (int): 请求超时时间（秒）。
            proxy (Optional[str]): 代理URL。
        """
        self.retries = retries
        self.retry_delay = retry_delay
        self.timeout = timeout
        self.proxy = proxy
        self.counter = Counter()
        self.logger = LoggerEx(self.__class__.__name__).get_logger()
        self.cache = {}

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    async def send_request(self, method: str, url: str, data: Optional[Dict[str, Any]] = None,
                           headers: Optional[Dict[str, str]] = None,
                           cookies: Optional[Dict[str, str]] = None) -> Response:
        cache_key = (method, url, str(data), str(headers), str(cookies))
        if cache_key in self.cache:
            return self.cache[cache_key]

        for attempt in range(self.retries):
            try:
                response = await self.session.request(
                    method=method,
                    url=url,
                    data=data,
                    headers=headers,
                    cookies=cookies,
                    proxy=self.proxy,
                    timeout=aiohttp.ClientTimeout(total=self.timeout)
                )
                async_response = Response(response.status, response.reason, self, response)
                self.cache[cache_key] = async_response
                await self.counter.increment_successful()
                return async_response
            except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                self.logger.error(f"Request to {url} failed on attempt {attempt + 1}: {str(e)}")
                if attempt == self.retries - 1:
                    await self.counter.increment_failed()
                    raise
                await asyncio.sleep(self.retry_delay)
            except Exception as e:
                self.logger.error(f"Unexpected error during request to {url}: {str(e)}")
                await self.counter.increment_failed()
                raise
        return Response(0, "Request Failed", self, None)

    async def get(self, url: str, headers: Optional[Dict[str, str]] = None,
                  cookies: Optional[Dict[str, str]] = None) -> Response:
        return await self.send_request("GET", url, headers=headers, cookies=cookies)

    async def post(self, url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None,
                   cookies: Optional[Dict[str, str]] = None) -> Response:
        return await self.send_request("POST", url, data=data, headers=headers, cookies=cookies)

#
# if __name__ == '__main__':
#     async def main():
#         async with AsyncRequest() as request:
#             response_get = await request.get("https://httpbin.org/get")
#             if response_get is not None:
#                 print(await response_get.text())
#             else:
#                 print("Request failed")
#
#
#     asyncio.run(main())
