import asyncio
from asyncio import (Queue, Task)
from random import randrange
from typing import List

from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response

routes = web.RouteTableDef()

QUEUE_KEY = "order_queue"
TASKS_KEY = "orders_tasks"


async def process_order_worker(worker_id: int, queue: Queue):
    while True:
        print(f"worker {worker_id}: waiting for an order")
        order = await queue.get()
        print(f"worker {worker_id}: processing order {order}")
        await asyncio.sleep(order)
        print(f"worker {worker_id}: processed order {order}")
        queue.task_done()


@routes.post("/order")
async def place_order(request: Request) -> Response:
    order_queue = app[QUEUE_KEY]
    await order_queue.put(randrange(5))

    return Response(body="order placed")


async def create_order_queue(app: Application):
    print("creating order queue and tasks.")
    queue: Queue = asyncio.Queue(10)
    app[QUEUE_KEY] = queue
    app[TASKS_KEY] = [asyncio.create_task(process_order_worker(i, queue)) for i in range(5)]


async def destroy_queue(app: Application):
    order_tasks: List[Task] = app[TASKS_KEY]
    queue: Queue = app[QUEUE_KEY]
    print(f"waiting for pending queue workers to finish")
    try:
        await asyncio.wait_for(queue.join(), timeout=10)
    finally:
        print("finished all pending items, canceling worker takss")


app = web.Application()
app.on_startup.append(create_order_queue)
app.on_shutdown.append(destroy_queue)
app.add_routes(routes)
web.run_app(app)
