import asyncio
import logging
import os
import sys
import tty
from asyncio import (StreamReader, StreamWriter)
from collections import deque

from message_store import MessageStore, read_line, EscapeSequence
from utils import create_stdin_reader


async def send_message(message: str, writer: StreamWriter):
    writer.write((message + "\n").encode())
    await writer.drain()


async def listen_for_messages(reader: StreamReader, message_store: MessageStore):
    while (message := await reader.readline()) != b"":
        await message_store.append(message.decode())
    await message_store.append("server closed connection.")


async def read_and_send(stdin_reader: StreamReader, writer: StreamWriter):
    while True:
        message = await read_line(stdin_reader)
        await send_message(message, writer)


async def main_listener():
    async def redraw_output(items: deque):
        EscapeSequence.save_cursor_position()
        EscapeSequence.move_back_one_char()
        for item in items:
            EscapeSequence.delete_line()
            sys.stdout.write(item)
        EscapeSequence.restore_cursor_position()

    tty.setcbreak(0)
    os.system("clear")
    rows = EscapeSequence.move_to_bottom_of_screen()
    messages = MessageStore(redraw_output, rows - 1)
    stdin_reader = await create_stdin_reader()
    sys.stdout.write("enter username: ")
    username = await read_line(stdin_reader)

    reader, writer = await asyncio.open_connection("localhost", 8000)

    writer.write(f"connect {username}\n".encode())
    await writer.drain()

    message_listener = asyncio.create_task(listen_for_messages(reader, messages))
    input_listener = asyncio.create_task(read_and_send(stdin_reader, writer))

    try:
        await asyncio.wait([message_listener, input_listener], return_when=asyncio.FIRST_COMPLETED)
    except Exception as e:
        logging.exception(e)
        writer.close()
        await writer.wait_closed()


class ChatServer:
    def __init__(self):
        self._username_to_writer = dict()

    async def start_chat_server(self, host: str, port: int):
        server = await asyncio.start_server(self.client_connected, host, port)
        async with server:
            await server.serve_forever()

    async def client_connected(self, reader: StreamReader, writer: StreamWriter):
        command = await reader.readline()
        print(f"connected {reader} {writer}")
        command, args = command.split(b" ")
        if command == b"CONNECT":
            username = args.replace(b"\n", b"").decode()
            self._add_user(username, reader, writer)
            await self._on_connect(username, writer)
        else:
            logging.error("got invalid command from client, disconnecting.")
            writer.close()
            await writer.wait_closed()

    def _add_user(self, username: str, reader: StreamReader, writer: StreamWriter):
        self._username_to_writer[username] = writer
        asyncio.create_task(self._listen_for_messages(username, reader))

    async def _on_connect(self, username: str, writer: StreamWriter):
        writer.write(f"welcome! {len(self._username_to_writer)} users are online!\n".encode())

        await writer.drain()
        await self._notify_all(f"{username} connected!\n")

    async def _remove_user(self, username: str):
        writer = self._username_to_writer[username]
        del self._username_to_writer[username]
        try:
            writer.close()
            await writer.wait_closed()
        except Exception as e:
            logging.exception("error closing client writer, ignoring.", exc_info=e)

    async def _listen_for_messages(self, username: str, reader: StreamReader):
        try:
            while (data := await asyncio.wait_for(reader.readline(), 60)) != b"":
                await self._notify_all(f"{username}: {data.encode()}")
            await self._notify_all(f"{username} has left the chat\n")
        except Exception as e:
            logging.exception("error reading from client", exc_info=e)
            await self._remove_user(username)

    async def _notify_all(self, message: str):
        inactive_users = list()
        for username, writer in self._username_to_writer.items():
            try:
                writer.write(message.encode())
                await writer.drain()
            except ConnectionError as e:
                logging.exception("couldn't write to client", exc_info=e)
                inactive_users.append(username)

        [await self._remove_user(username) for username in inactive_users]


async def main():
    chat_server = ChatServer()
    await chat_server.start_chat_server("localhost", 8000)


if __name__ == "__main__":
    asyncio.run(main())
