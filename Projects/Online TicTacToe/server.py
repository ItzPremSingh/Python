from socket import AF_INET, SOCK_STREAM

from helper import server_starter, socket
from setting import HOST, PORT

if __name__ == "__main__":
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((HOST, PORT))

    server.listen()

    server_starter(server)
