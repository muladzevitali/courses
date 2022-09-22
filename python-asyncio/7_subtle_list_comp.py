import asyncio

from utils import async_timed, delay


@async_timed()
async def main() -> None:
    delay_times = (3, 3, 3, 4)
    tasks = [asyncio.create_task(delay(time)) for time in delay_times]
    [await task for task in tasks]


if __name__ == "__main__":
    asyncio.run(main())
