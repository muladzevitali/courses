import asyncio
import signal
from asyncio import AbstractEventLoop
from typing import Set, List, Optional


class GracefulExit(SystemExit):
    pass


def shutdown():
    raise GracefulExit()


def cancel_tasks():
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    _ = [task.cancel() for task in tasks]


async def await_for_all_tasks():
    tasks: Set[asyncio.Task] = asyncio.all_tasks()
    _ = [await task for task in tasks]


async def close_echo_tasks(echo_tasks: Optional[List[asyncio.Task]]):
    waiters = [asyncio.wait_for(task, 2) for task in echo_tasks]
    for task in waiters:
        try:
            await task
        except asyncio.exceptions.TimeoutError:
            pass


async def main():
    loop: AbstractEventLoop = asyncio.get_running_loop()

    loop.add_signal_handler(signal.SIGINT, cancel_tasks)
    loop.add_signal_handler(signal.SIGINT, lambda: asyncio.create_task(await_for_all_tasks()))
    await asyncio.sleep(10)


async def main_2():
    loop: AbstractEventLoop = asyncio.get_running_loop()

    loop.add_signal_handler(signal.SIGINT, shutdown)
    try:
        ...
    except GracefulExit:
        loop.run_until_complete(close_echo_tasks([]))
    finally:
        loop.close()


if __name__ == "__main__":
    asyncio.run(main())
