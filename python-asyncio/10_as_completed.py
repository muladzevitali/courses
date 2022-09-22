import asyncio
import time

import aiohttp

from utils import (async_timed, fetch_status)


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = (
            fetch_status(session, "https://example.com", 1),
            fetch_status(session, "https://example.com", 1),
            fetch_status(session, "python://example.com", 10)
        )
        for finished_task in asyncio.as_completed(fetchers, timeout=3):
            try:
                start = time.time()
                result = await finished_task
                print(result, time.time() - start)
            except asyncio.exceptions.TimeoutError:
                print("we've got an exception")

        for task in asyncio.tasks.all_tasks():
            print(task)


if __name__ == "__main__":
    asyncio.run(main())
