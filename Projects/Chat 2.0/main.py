from threading import Thread

from helper import Connect

RUNNING = True


def handleReceive(connect: Connect) -> None:
    """handle all receive message from server"""

    while RUNNING:
        print("\nServer > ", connect.receive())


def handleSend(connect: Connect) -> None:
    """handle sending message to server"""
    global RUNNING

    while RUNNING:
        message = input("Client > ")
        while message == "":
            message = input("Client > ")

        if message == "quit":
            RUNNING = False
            break

        connect.send(message + "\n")


connect = Connect("192.168.95.119", 8080)

Thread(target=handleReceive, args=(connect,)).start()


handleSend(connect)
connect.close()
quit()