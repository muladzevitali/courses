import asyncio
import logging

import aiohttp

from utils import (async_timed, fetch_status)


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = (
            asyncio.create_task(fetch_status(session, "https://example.com")),
            asyncio.create_task(fetch_status(session, "python://example.com", 19))
        )
        done, pending = await asyncio.wait(fetchers)

        print(f"done task count: {len(done)}")
        print(f"pending task count: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("request got an exception", exc_info=done_task.exception())


if __name__ == "__main__":
    asyncio.run(main())
