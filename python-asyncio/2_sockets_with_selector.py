import selectors
import socket
from selectors import SelectorKey
from typing import List, Tuple


selector = selectors.DefaultSelector()

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("localhost", 8000)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)

while True:
    events: List[Tuple[SelectorKey, int]] = selector.select(timeout=1)
    if len(events) == 0:
        print("no events, waiting a bit more")

    for event, _ in events:
        event_socket = event.fileobj
        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            event_socket.send(data)

