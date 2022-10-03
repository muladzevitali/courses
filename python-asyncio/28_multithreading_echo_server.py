import socket
from threading import Thread


class ClientEchoThread(Thread):
    def __init__(self, client):
        super(ClientEchoThread, self).__init__()
        self.client = client

    def run(self):
        try:
            while True:
                data = self.client.recv(2048)
                if not data:
                    raise BrokenPipeError("connection closed")

                print(f"received {data}, sending")
                self.client.sendall(data)

        except OSError as e:
            print(f"thread interrupted by {e} exception, shutting down")

    def close(self):
        if self.is_alive():
            self.client.sendall(bytes("shutting down!", encoding="utf-8"))
            self.client.shutdown(socket.SHUT_RDWR)


def echo(client: socket):
    while True:
        data = client.recv(2048)
        print(f"received {data}, sending!")
        client.sendall(data)


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("localhost", 8000))
        server.listen()
        connection_threads = list()
        try:
            while True:
                connection, _ = server.accept()
                thread = ClientEchoThread(connection)
                connection_threads.append(thread)
                thread.start()
        except KeyboardInterrupt:
            print("shutting down")
            [thread.close() for thread in connection_threads]
