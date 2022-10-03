import asyncio
import functools
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

import requests

from utils import async_timed

counter_lock = Lock()
counter: int = 0


def get_status_code(url: str) -> int:
    global counter
    response = requests.get(url)
    with counter_lock:
        counter += 1

    return response.status_code


async def reporter(request_count: int):
    while counter < request_count:
        print(f"finished {counter}/{request_count} requests")
        await asyncio.sleep(.5)


@async_timed()
async def main():
    request_count = 200
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        urls = ["https://example.com" for _ in range(request_count)]

        reporter_task = asyncio.create_task(reporter(request_count))
        tasks = [loop.run_in_executor(pool, functools.partial(get_status_code, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        await reporter_task

        print(results)


if __name__ == "__main__":
    asyncio.run(main())
