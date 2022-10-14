import asyncio
from asyncio import (StreamReader, StreamWriter, Event)
from asyncio.subprocess import Process


async def output_consumer(input_ready_event: Event, stdout: StreamReader):
    while (data := await stdout.read(1024)) != b"":
        print(data)
        if data.decode().endswith("enter text to echo: "):
            input_ready_event.set()


async def input_writer(text_data, input_ready_event: Event, stdin: StreamWriter):
    for text in text_data:
        await input_ready_event.wait()
        stdin.write(text.encode())
        await stdin.drain()
        input_ready_event.clear()


async def main():
    program = ("python", "echo_input.py")
    process: Process = await asyncio.create_subprocess_exec(*program,
                                                            stdout=asyncio.subprocess.PIPE,
                                                            stdin=asyncio.subprocess.PIPE)
    input_ready_event = asyncio.Event()
    text_input = ("one\n", "two\n", "three\n", "four\n")

    await asyncio.gather(output_consumer(input_ready_event, process.stdout),
                         input_writer(text_input, input_ready_event, process.stdin),
                         process.wait()
                         )


if __name__ == '__main__':
    asyncio.run(main())
