from random import choice
from re import search

position = [" " for _ in range(9)]
whiteSpace = [_ for _ in range(9)]

compPostion = []
userPosition = []


def display(position: list) -> None:
    print(" | ".join(position[0:3]))
    print("—————————")
    print(" | ".join(position[3:6]))
    print("—————————")
    print(" | ".join(position[6:9]))


def isFilled(position: list, index: int) -> bool:
    if position[index] == " ":
        return False

    return True


def isDraw(position: list) -> bool:
    if " " in position:
        return False

    return True


def fill(position: list, index: int, char: str, whiteSpace: list) -> None:
    whiteSpace.remove(index)
    position[index] = char


def intInput(prompt: str = "") -> int:
    while True:
        data = input(prompt)
        if reSearch := search(r"\s*(?P<number>\d+)\s*", data):
            return int(reSearch.group("number"))


def isWon(position: list) -> bool:
    _ = position

    if (
        _[0] == _[1] == _[2] != " "
        or _[3] == _[4] == _[5] != " "
        or _[6] == _[7] == _[8] != " "
    ):
        return True

    if (
        _[0] == _[3] == _[6] != " "
        or _[1] == _[4] == _[7] != " "
        or _[2] == _[5] == _[8] != " "
    ):
        return True

    if _[0] == _[4] == _[8] != " " or _[2] == _[4] == _[6] != " ":
        return True

    return False


def isStarted(position: list) -> bool:
    for char in position:
        if char != " ":
            return False
    return True


def compEdge(index: int) -> list:
    edge = {
        0: [2, 6],
        2: [0, 8],
        6: [0, 8],
        8: [2, 6],
    }

    return edge[index]


def inList(__list: list, elements: list | int) -> None:
    if type(elements) == list:
        for element in elements:
            if element in __list:
                __list.remove(element)

    else:
        if elements in __list:
            __list.remove(elements)


def anyNotFilled(position, __list: list) -> int:
    _list = []
    for element in __list:
        if not isFilled(position, element):
            _list.append(element)

    return choice(_list)  # not element left


def postionComplete(position: list, whiteSpace: list) -> int:
    _ = position

    if (
        _[1] == _[2] != " " or _[3] == _[6] != " " or _[4] == _[8] != " "
    ) and not isFilled(position, 0):
        return 0

    elif (_[0] == _[2] != " " or _[4] == _[7] != " ") and not isFilled(position, 1):
        return 1

    elif (
        _[0] == _[1] != " " or _[5] == _[8] != " " or _[4] == _[6] != " "
    ) and not isFilled(position, 2):
        return 2

    elif (_[0] == _[6] != " " or _[4] == _[5] != " ") and not isFilled(position, 3):
        return 3

    elif (
        _[0] == _[8] != " " or _[1] == _[7] != " " or _[2] == _[6] != " "
    ) and not isFilled(position, 4):
        return 4

    elif (_[2] == _[8] != " " or _[3] == _[4] != " ") and not isFilled(position, 5):
        return 5

    elif (
        _[0] == _[3] != " " or _[7] == _[8] != " " or _[4] == _[2] != " "
    ) and not isFilled(position, 6):
        return 6

    elif (_[4] == _[1] != " " or _[6] == _[8] != " ") and not isFilled(position, 7):
        return 7

    elif (
        _[2] == _[5] != " " or _[6] == _[7] != " " or _[0] == _[4] != " "
    ) and not isFilled(position, 8):
        return 8

    else:
        return choice(whiteSpace)


def compTurn(
    position: list, whiteSpace: list, turn: int, compPostion: list, userPosition: list
) -> int:
    userPos = userPosition[-1]
    edgePosition = [0, 2, 6, 8]
    _ = position

    if turn == 0:  # Computer first
        return choice(edgePosition)

    elif turn == 1:  # User first past
        inList(edgePosition, userPos)
        return choice(edgePosition)

    elif turn == 2:  # Computer second
        inList(edgePosition, userPos)
        edgePos = compEdge(compPostion[-1])

        return anyNotFilled(position, edgePos)

    elif turn == 3:  # User second past
        inList(edgePosition, userPosition)
        inList(edgePosition, compPostion)
        if edgePosition:
            edgePos = compEdge(edgePosition[-1])

            return anyNotFilled(position, edgePos)

        else:
            return postionComplete(position, whiteSpace)

    return postionComplete(position, whiteSpace)


userChar = "O"
compChar = "X"

for turn in range(1, 10):
    display(position)
    while True:
        index = intInput("Enter your index: ") - 1
        if index in range(9):
            if not isFilled(position, index):
                fill(position, index, userChar, whiteSpace)
                userPosition.append(index)
                break

    if isWon(position):
        print("User Won")
        break

    compIndex = compTurn(position, whiteSpace, turn, compPostion, userPosition)
    fill(position, compIndex, compChar, whiteSpace)
    compPostion.append(compIndex)

    if isWon(position):
        print("Computer Won")
        break
