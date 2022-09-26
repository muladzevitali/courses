import asyncio
import functools
import time
from typing import Callable, Any

from aiohttp import ClientSession
import asyncpg


def async_timed():
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"starting function {func} with args {args} kwargs {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"finished {func} in {total:.4f} second(s)")

        return wrapped

    return wrapper


@async_timed()
async def delay(seconds):
    print(f"sleeping for {seconds} second(s)")
    await asyncio.sleep(seconds)
    print(f"finished sleeping for {seconds} second(s)")
    return seconds


@async_timed()
async def fetch_status(session: ClientSession, url: str, delay_seconds: int = 0) -> int:
    await asyncio.sleep(delay_seconds)
    async with session.get(url) as result:
        return result.status


async def get_postgres_connection():
    return await asyncpg.connect(host="localhost", port=5432, database="products", password="password")
