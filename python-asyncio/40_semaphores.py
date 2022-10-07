import asyncio
from asyncio import Semaphore
from aiohttp import ClientSession


async def get_url(url: str, session: ClientSession, semaphore: Semaphore):
    print(f"waiting to acquire semaphore")
    async with semaphore:
        print("acquired semaphore, requesting...")
        response = await session.get(url)
        print("finished requesting")
        return response.status


async def main():
    semaphore = Semaphore(10)  # semaphore = BoundedSemaphore(1)
    async with ClientSession() as session:
        tasks = [get_url("https://example.com", session, semaphore) for _ in range(100)]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
