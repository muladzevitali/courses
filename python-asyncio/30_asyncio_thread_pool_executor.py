import asyncio
import functools
from concurrent.futures import ThreadPoolExecutor

import requests

from utils import async_timed


def get_status_code(url: str) -> int:
    response = requests.get(url)
    return response.status_code


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        urls = ["https://example.com" for _ in range(1000)]
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        print(results)


@async_timed()
async def main_2():
    loop = asyncio.get_running_loop()
    urls = ["https://example.com" for _ in range(1000)]
    tasks = [loop.run_in_executor(None, functools.partial(get_status_code, url)) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
