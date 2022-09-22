import asyncio
import logging

import aiohttp

from utils import (fetch_status, async_timed)


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        fetchers = (
            asyncio.create_task(fetch_status(session, "python://bad.com")),
            asyncio.create_task(fetch_status(session, "https://example.com", delay_seconds=3)),
            asyncio.create_task(fetch_status(session, "https://example.com", delay_seconds=3))
        )

        done, pending = await asyncio.wait(fetchers, return_when=asyncio.FIRST_EXCEPTION)

        print(f"done tasks count: {len(done)}")
        print(f"pending tasks count: {len(pending)}")

        for done_task in done:
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("request got an exception", exc_info=done_task.exception())

        for pending_task in pending:
            pending_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())