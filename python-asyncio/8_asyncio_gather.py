import asyncio

from aiohttp import ClientSession

from utils import (fetch_status, async_timed, delay)


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ["https://example.com" for _ in range(1_000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


async def main_2():
    results = await asyncio.gather(delay(5), delay(1))

    print(results)


if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(main_2())
