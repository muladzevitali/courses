import asyncio
import os
import sys
import tty
from asyncio import StreamReader
from collections import deque
from typing import (Callable, Deque, Awaitable)

from escape_sequence import EscapeSequence
from utils import create_stdin_reader


class MessageStore:
    def __init__(self, callback: Callable[[Deque], Awaitable[None]], max_size: int):
        self._deque = deque(maxlen=max_size)
        self._callback = callback

    async def append(self, item):
        self._deque.append(item)
        await self._callback(self._deque)


async def sleep(delay: int, message_store: MessageStore):
    await message_store.append(f"starting delay {delay}")
    await asyncio.sleep(delay)


async def read_line(stdin_reader: StreamReader):
    def erase_last_char():
        EscapeSequence.move_back_one_char()
        sys.stdout.write(" ")
        EscapeSequence.move_back_one_char()

    delete_char = b"\x7f"
    input_buffer = deque()
    while (input_char := await stdin_reader.read(1)) != b"\n":
        if input_char == delete_char:
            if len(input_buffer) > 0:
                input_buffer.pop()
                erase_last_char()
                sys.stdout.flush()

        else:
            input_buffer.append(input_char)
            sys.stdout.write(input_char.decode())
            sys.stdout.flush()
    print("clearing line")
    EscapeSequence.clear_line()
    print("cleared")
    return b"".join(input_buffer).decode()


async def main():
    tty.setcbreak(sys.stdin)
    os.system("clear")
    rows = EscapeSequence.move_to_bottom_of_screen()

    async def redraw_output(items: Deque):
        EscapeSequence.save_cursor_position()
        EscapeSequence.move_to_top_of_screen()
        for item in items:
            EscapeSequence.delete_line()
            print(item)
        EscapeSequence.restore_cursor_position()

    messages = MessageStore(redraw_output, rows - 1)
    stdin_reader = await create_stdin_reader()

    while True:
        line = await read_line(stdin_reader)
        print(line)
        delay_time = int(line)
        asyncio.create_task(sleep(delay_time, messages))


if __name__ == "__main__":
    asyncio.run(main())
