import asyncio

import aiohttp
from aiohttp import ClientSession

from utils import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    one_second = aiohttp.ClientTimeout(total=1)
    async with session.get(url, timeout=one_second) as result:
        return result.status


@async_timed()
async def main():
    session_timeout = aiohttp.ClientTimeout(total=2, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        url = "https://example.com"
        status = await fetch_status(session, url)
        print(f"status for {url} was {status}")


asyncio.run(main())
