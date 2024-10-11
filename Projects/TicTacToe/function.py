from socket import socket


def clientHandler(client: socket) -> None:
    client.send("hello".encode())

    client.close()
