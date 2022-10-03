import asyncio

from utils import (create_stdin_reader, delay)


async def main():
    stdin_reader = await create_stdin_reader()
    while True:
        delay_time = await stdin_reader.readline()
        asyncio.create_task(delay(int(delay_time)))


if __name__ == "__main__":
    asyncio.run(main())
