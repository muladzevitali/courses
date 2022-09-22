import asyncio

import aiohttp

from utils import (fetch_status, async_timed)


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = (
            asyncio.create_task(fetch_status(session, "https://example.com", delay_seconds=0)),
            asyncio.create_task(fetch_status(session, "https://example.com", delay_seconds=0)),
            asyncio.create_task(fetch_status(session, "https://example.com", delay_seconds=3))
        )
        done, pending = await asyncio.wait(fetchers, timeout=1)

        print(f"done task count: {len(done)}")
        print(f"pending task count: {len(pending)}")

        for done_task in done:
            result = await done_task
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
