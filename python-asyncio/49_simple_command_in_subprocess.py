import asyncio
from asyncio.subprocess import Process
from asyncio import StreamReader


async def main():
    process: Process = await asyncio.create_subprocess_exec("ls", "-l")
    print(f"process pid is: {process.pid}")
    status_code = await process.wait()
    print(f"status code: {status_code}")


async def write_output(prefix: str, stdout: StreamReader):
    while line := await stdout.readline():
        print(f"[{prefix}]: {line.rstrip().decode()}")


async def sleep():
    process: Process = await asyncio.create_subprocess_exec("sleep", "3")
    print(f"process pid is: {process.pid}")

    try:
        status_code = await asyncio.wait_for(process.wait(), timeout=1)
        print(status_code)
    except  asyncio.TimeoutError:
        print("timeout waiting to finish, terminating")
        process.terminate()
        status_code = await process.wait()
        print(status_code)


async def main_write_output():
    program = ("ls", "-l")
    process: Process = await asyncio.create_subprocess_exec(*program, stdout=asyncio.subprocess.PIPE)
    print(f"process pid is: {process.pid}")
    stdout_task = asyncio.create_task(write_output(" ".join(program), process.stdout))
    return_code, _ = await asyncio.gather(process.wait(), stdout_task)
    print(f"process returned: {return_code}")


if __name__ == "__main__":
    asyncio.run(main_write_output())
