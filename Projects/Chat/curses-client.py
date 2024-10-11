import socket
from curses import newwin, wrapper
from curses.ascii import isprint
from threading import Thread

import helper


def handleRecv(sock, seprater, stdscr, textbox):
    height, width = stdscr.getmaxyx()
    centerX = width // 2
    msgPosition = height - 8
    leftLine = 3

    while True:
        textbox.border()

        if msgPosition < 3:
            msgPosition = height - 8
            stdscr.clear()
            textbox.border()

        data = helper.receiver(sock)
        if not data:
            break

        msgSplited = data.split(seprater)
        msgSplitLen = len(msgSplited)

        if msgSplitLen == 3:
            server, clientName, msg = msgSplited
            stdscr.addstr(msgPosition, centerX, f"{clientName} {msg}")

        elif msgSplitLen == 2:
            name, msg = msgSplited
            stdscr.addstr(msgPosition, 0, f"{name}: {msg}")

        else:
            continue

        stdscr.refresh()

        msgPosition -= leftLine


def wrap(text, width):
    listOfWord = []
    totalLen = len(text)
    totalNum = 1
    number = 1
    _text = ""

    for letter in text:
        _text += letter

        if totalNum == totalLen:
            listOfWord.append(_text)

        elif number == width:
            listOfWord.append(_text)
            number = 0
            _text = ""

        number += 1
        totalNum += 1

    return listOfWord


host = helper.host
port = helper.port
close = helper.close
seprater = helper.seprater

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

name = input("Enter Name: ")
helper.sender(sock, helper.jsonBuilder(name="name"))


def main(stdscr):
    height, width = stdscr.getmaxyx()
    inputList = []
    boxHeight = 5
    winHeight = height - boxHeight
    maxWidth = width - 2
    maxText = (boxHeight - 2) * maxWidth
    textbox = newwin(0, 0, winHeight, 0)
    textbox.border()
    textbox.addstr(1, 1, "")
    line = 1

    handler = Thread(target=handleRecv, args=(sock, seprater, stdscr, textbox))
    handler.start()

    while True:
        textbox.refresh()

        try:
            char = textbox.getch()
        except KeyboardInterrupt:
            break

        if char == 10:  # Enter
            if inputList:
                data = "".join(inputList)
                textbox.clear()
                textbox.border()
                inputList.clear()

                helper.sender(sock, data)

                if data == close:
                    break

            else:
                continue

        elif char == 127:  # Delete
            if inputList:
                textbox.clear()
                textbox.border()
                inputList.pop()

            else:
                continue

        elif isprint(char) and len("".join(inputList)) != maxText:  # Printable
            inputList.append(chr(char))

        msg = "".join(inputList)
        msgSplited = wrap(msg, maxWidth)
        msgLen = len(msgSplited)

        if msgLen == 0:
            textbox.addstr(1, 1, "")
            continue

        for line in range(msgLen):
            textbox.addstr(line + 1, 1, msgSplited[line])


wrapper(main)
