import asyncio

import aiohttp

from utils import (fetch_status, async_timed)


@async_timed()
async def main():
    url = "https://example.com"
    async with aiohttp.ClientSession() as session:
        fetchers = [asyncio.create_task(fetch_status(session, url)) for _ in range(3)]
        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_COMPLETED)

        print(f"done task count: {len(done)}")
        print(f"pending task count: {len(pending)}")

        for done_task in done:
            print(await done_task)


@async_timed()
async def main_2():
    url = "https://example.com"

    async with aiohttp.ClientSession() as session:
        pending = [
            asyncio.create_task(fetch_status(session, url)) for _ in range(3)
        ]
        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
            print(f"done task count: {len(done)}")
            print(f"pending task count: {len(pending)}")

            for done_task in done:
                print(await done_task)


if __name__ == "__main__":
    asyncio.run(main_2())
