import asyncio
from asyncio import StreamReader, StreamWriter


class FileUpload:
    def __init__(self, reader: StreamReader, writer: StreamWriter):
        self._reader = reader
        self._writer = writer
        self._finished_event = asyncio.Event()
        self._buffer = b""
        self._upload_task = None

    def listen_for_uploads(self):
        self._upload_task = asyncio.create_task(self._accept_upload())

    async def _accept_upload(self):
        while data := await self._reader.read(1024):
            self._buffer += data

        self._finished_event.set()
        self._writer.close()
        await self._writer.wait_closed()

    async def get_contents(self):
        await self._finished_event.wait()
        return self._buffer


class FileServer:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.upload_event = asyncio.Event()

    async def start_server(self):
        server = await asyncio.start_server(self._client_connected, self.host, self.port)
        await server.serve_forever()

    async def dump_contents_on_complete(self, upload: FileUpload):
        file_contents = await upload.get_contents()
        print(file_contents)

    def _client_connected(self, reader: StreamReader, writer: StreamWriter):
        upload = FileUpload(reader, writer)
        upload.listen_for_uploads()
        asyncio.create_task(self.dump_contents_on_complete(upload))


async def main():
    server = FileServer("localhost", 9000)
    await server.start_server()


if __name__ == "__main__":
    asyncio.run(main())
