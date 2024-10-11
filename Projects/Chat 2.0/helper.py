from socket import AF_INET, SOCK_STREAM, socket


class Server:
    def __init__(self, host: str, port: int = 8000) -> None:
        """start server on host:port if idle"""

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((host, port))

        self.sock.listen()

    def accept(self) -> tuple[socket, tuple[int, int]]:
        """accept incomming connection else wait"""

        return self.sock.accept()

    def close(self) -> None:
        """shutdown server"""

        self.sock.shutdown(0)


class Client:
    def __init__(self, client: socket) -> None:
        """easy to handle client"""

        self._client = client

    def send(self, message: str) -> int:
        """send message to connection"""

        return self._client.send(message.encode())

    def receive(self, bufsize: int = 1024) -> str:
        """return received data form sock"""

        return self._client.recv(bufsize).decode()

    def close(self) -> None:
        """close connection from server"""

        self._client.close()


class Connect(Client):
    def __init__(self, host: str, port: int = 8000) -> None:
        """stablize connection"""

        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.connect((host, port))

        super().__init__(self.server)
