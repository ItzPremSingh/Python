from socket import AF_INET, SOCK_STREAM, socket
from sys import argv
from threading import Thread

import helper

if argv[1::]:
    name = argv[1]

else:
    try:
        name = input("Enter Name: ")

    except (Exception, KeyboardInterrupt):
        quit(1)


def handleRecv(sock):
    while True:
        data = helper.receiver(sock)
        if not data:
            break

        jsonData = helper.jsonExt(data)
        name = jsonData.get("name")
        data = jsonData.get("data")

        print("\033[F", end="\033[K")

        if not name:
            name = "<directly> " + jsonData.get("by")

        if data:
            print(f"{recvColor}{name}: {data}\33[m")

        else:
            event = jsonData.get("event")
            print(helper.center(f"{name} {event}", msgColor))

        print("Enter Message: ")


msgColor = helper.msgColor
recvColor = helper.recvColor
host = helper.host
port = helper.port
close = helper.close


sock = socket(AF_INET, SOCK_STREAM)
sock.connect((host, port))

helper.sender(sock, helper.jsonBuilder(name=name))


handler = Thread(target=handleRecv, args=(sock,))
handler.start()

while True:
    try:
        data = input("Enter Message: ")
        if data == "":
            continue

    except (Exception, KeyboardInterrupt):
        helper.sender(sock, close)
        print("Disconnected!")
        break

    try:
        helper.sender(sock, data)
    except BrokenPipeError:
        print("Server closed!")
        data = close

    if data == close:
        break
