import asyncio
import tkinter
from asyncio import AbstractEventLoop
from concurrent.futures import Future
from queue import Queue
from threading import Thread
from tkinter import ttk
from typing import (Callable, Optional)

from aiohttp import ClientSession

window = tkinter.Tk()
window.title("Hello world app")
window.geometry("200x100")


class StressTest:
    def __init__(self, loop: AbstractEventLoop, url: str, total_requests: int,
                 callback: Callable[[int, int], None]):
        self._completed_requests: int = 0
        self._load_test_future: Optional[Future] = None
        self._loop = loop
        self._url: str = url
        self._total_requests: int = total_requests
        self._callback = callback
        self._refresh_rate = total_requests // 100

    def start(self):
        future = asyncio.run_coroutine_threadsafe(self._make_requests(), self._loop)
        self._load_test_future = future

    def cancel(self):
        if self._load_test_future:
            self._loop.call_soon_threadsafe(self._load_test_future.cancel)

    async def _get_url(self, session: ClientSession, url: str):
        try:
            await session.get(url)
        except Exception as e:
            print(e)

        self._completed_requests += 1
        if self._completed_requests % self._refresh_rate == 0 \
                or self._completed_requests == self._total_requests:
            self._callback(self._completed_requests, self._total_requests)

    async def _make_requests(self):
        async with ClientSession() as session:
            reqs = [self._get_url(session, self._url) for _ in range(self._total_requests)]
            await asyncio.gather(*reqs)


class LoadTester(tkinter.Tk):
    def __init__(self, loop, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._queue = Queue()
        self._refresh_ms = 25

        self._loop = loop
        self._load_test: Optional[StressTest] = None
        self.title("URL Requester")

        self._url_label = tkinter.Label(self, text="URL:")
        self._url_label.grid(column=0, row=0)

        self._url_field = tkinter.Entry(self, width=10)
        self._url_field.grid(column=1, row=0)

        self._request_label = tkinter.Label(self, text="Number of requests:")
        self._request_label.grid(column=0, row=1)

        self._request_field = tkinter.Entry(self, width=10)
        self._request_field.grid(column=1, row=1)

        self._submit = ttk.Button(self, text="Submit", command=self._start)
        self._submit.grid(column=2, row=1)

        self._pb_label = tkinter.Label(self, text="Progress:")
        self._pb_label.grid(column=0, row=3)

        self._pb = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self._pb.grid(column=1, row=3, columnspan=2)

    def _update_bar(self, percentage: int):
        if percentage == 100:
            self._load_test = None
            self._submit["text"] = "Submit"
        else:
            self._pb["value"] = percentage
            self.after(self._refresh_ms, self._poll_queue)

    def _queue_update(self, completed_requests: int, total_requests: int):
        self._queue.put(int(completed_requests / total_requests * 100))

    def _poll_queue(self):
        if not self._queue.empty():
            percent_complete = self._queue.get()
            self._update_bar(percent_complete)
        else:
            if self._load_test:
                self.after(self._refresh_ms, self._poll_queue)

    def _start(self):
        if self._load_test is None:
            self._submit["text"] = "Cancel"
            test = StressTest(self._loop, self._url_field.get(),
                              int(self._request_field.get()), self._queue_update)
            self.after(self._refresh_ms, self._poll_queue)
            test.start()
            self._load_test = test
        else:
            self._load_test.cancel()
            self.load_test = None
            self._submit["text"] = "Submit"


class ThreadedEventLoop(Thread):
    def __init__(self, loop: AbstractEventLoop):
        super().__init__()
        self._loop = loop
        self.daemon = True

    def run(self):
        self._loop.run_forever()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()

    asyncio_thread = ThreadedEventLoop(loop)
    asyncio_thread.start()

    app = LoadTester(loop)
    app.mainloop()
