from json import dumps, loads
from json.decoder import JSONDecodeError
from random import shuffle
from socket import socket
from threading import Thread
from typing import Any, Literal

from common import CHARS, Char, Code

won_conditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


def encoder(data: dict[str, Any]) -> bytes:
    return dumps(data).encode()


def decoder(data: bytes) -> dict[str, Any]:
    return loads(data)


def is_draw(board_position: list[str]) -> bool:
    for char in board_position:
        if char not in CHARS:
            return False

    return True


def is_won(board_position: list[str], char: str) -> bool:
    for i1, i2, i3 in won_conditions:
        if board_position[i1] == board_position[i2] == board_position[i3] == char:
            return True

    return False


def display_game_board(board_position: list[str]) -> None:
    _ = board_position
    board = (
        f"| {_[0]} | {_[1]} | {_[2]} |\n"
        "|-----------|\n"
        f"| {_[3]} | {_[4]} | {_[5]} |\n"
        "|-----------|\n"
        f"| {_[6]} | {_[7]} | {_[8]} |\n"
    )
    print(board)


def int_input(prompt: str = "") -> int:
    while True:
        try:
            _input = int(input(prompt))
            return _input

        except ValueError:
            ...


def handle_client(
    client: socket, friend: socket, chance: Literal[1, 0], char: str
) -> None:
    client.send(encoder({Code.CHANCE_CODE: chance, Code.CHAR_CODE: char}))

    for _ in range(int(5 if chance else 4)):
        try:
            recived_data = decoder(client.recv(1024))

        except JSONDecodeError:
            break

        friend.sendall(encoder(recived_data))

        if recived_data[Code.MATCH_CODE] != Char.MATCH_NORMAL_CHAR:
            break


def handle_friends(_friends: tuple[socket, socket]) -> None:
    turn_list = [0, 1]
    char_list = CHARS
    shuffle(turn_list)
    shuffle(char_list)

    Thread(target=handle_client, args=(*_friends, turn_list[0], char_list)).start()
    Thread(
        target=handle_client, args=(*_friends[::-1], turn_list[1], char_list[::-1])
    ).start()


def server_starter(server: socket) -> None:
    friends: list[tuple[socket, socket]] = []
    waiting_client: socket | None = None

    while True:
        try:
            client, _ = server.accept()

        except KeyboardInterrupt:
            server.shutdown(0)
            quit(0)

        if waiting_client is None:
            waiting_client = client
            client.send(encoder({Code.FRIEND_CODE: 0}))

        else:
            friends.append((waiting_client, client))
            client.send(encoder({Code.FRIEND_CODE: 1}))
            waiting_client.send(encoder({Code.FRIEND_CODE: 1}))

            Thread(target=handle_friends, args=((client, waiting_client),)).start()

            waiting_client = None
