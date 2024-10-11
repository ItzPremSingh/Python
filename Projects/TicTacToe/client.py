from socket import socket, AF_INET, SOCK_STREAM

from setting import HOST, PORT


sock = socket(AF_INET, SOCK_STREAM)

sock.connect((HOST, PORT))

print(sock.recv(1024).decode())

sock.close()
