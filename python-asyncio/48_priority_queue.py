import asyncio
from asyncio import (Queue, PriorityQueue)
from dataclasses import (dataclass, field)


@dataclass(order=True)
class WorkItem:
    priority: int
    data: str = field(compare=False)


async def worker(queue: Queue):
    while not queue.empty():
        work_item: WorkItem = await queue.get()
        print(f"processing work item {work_item}")
        queue.task_done()


async def main():
    priority_queue = PriorityQueue()
    work_items = [
        WorkItem(1, "high priority"),
        WorkItem(2, "medium priority"),
        WorkItem(3, "lowers priority")
    ]
    worker_task = asyncio.create_task(worker(priority_queue))
    for work in work_items:
        priority_queue.put_nowait(work)

    await asyncio.gather(priority_queue.join(), worker_task)


if __name__ == "__main__":
    asyncio.run(main())
