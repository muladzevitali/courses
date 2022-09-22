import asyncio

import aiohttp

from utils import (fetch_status, async_timed)


@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        urls = ("https://example.com", "python://example.com")
        tasks = (fetch_status(session, url) for url in urls)
        results = await asyncio.gather(*tasks, return_exceptions=True)

        exceptions = [result for result in results if isinstance(result, Exception)]
        successful_results = [result for result in results if not isinstance(result, Exception)]

        print(f"all results {results}")
        print(f"successful results {successful_results}")
        print(f"threw exceptions {exceptions}")


if __name__ == "__main__":
    asyncio.run(main())
