from re import search
from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread

import helper

ThreadRunning = True
pattern = r"^\s{0,}<(.+)>\s{0,}(.*)\s{0,}$"


def sendToAll(clientList, msg, client):
    for _client in clientList:
        if _client != client:
            helper.sender(_client, msg)


def handleClient(client, clientList, clientDict):
    data = helper.receiver(client)
    jsonData = helper.jsonExt(data)
    name = jsonData.get("name")

    if not name:
        clientList.remove(client)
        client.close()
        return 1

    clientDict.setdefault(name, client)

    sendToAll(
        clientList,
        helper.jsonBuilder(name=name, event="Joined"),
        client,
    )
    print(helper.center(f"{name} Joined", msgColor))

    global ThreadRunning

    while ThreadRunning:
        data = helper.receiver(client)
        if data == MsgClose or not data or not ThreadRunning:
            break
        match = search(pattern, data)

        if match:
            to, data = match.groups()
            sendTo = clientDict.get(to)
            if sendTo:
                helper.sender(sendTo, helper.jsonBuilder(by=name, data=data))
                print(f"{recvColor}{name} to {to}: ********")

        else:
            sendToAll(clientList, helper.jsonBuilder(name=name, data=data), client)
            print(f"{recvColor}{name}: {data}\33[m")

    sendToAll(clientList, helper.jsonBuilder(name=name, event="Left"), client)
    print(helper.center(f"{name} Left", msgColor))
    clientList.remove(client)
    client.close()


host = helper.host
msgColor = helper.msgColor
recvColor = helper.recvColor
port = helper.port
MsgClose = helper.close


sock = socket(AF_INET, SOCK_STREAM)
sock.bind((host, port))

sock.listen(10)

print("Chat server started")
clientList = []
clientDict = {}
while True:
    try:
        client, (host, port) = sock.accept()
    except (Exception, KeyboardInterrupt):
        ThreadRunning = False
        break

    clientList.append(client)
    handler = Thread(
        target=handleClient,
        args=(
            client,
            clientList,
            clientDict,
        ),
    )
    handler.start()

sock.close()
