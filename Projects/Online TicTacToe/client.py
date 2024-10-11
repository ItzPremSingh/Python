from socket import AF_INET, SOCK_STREAM

from common import Char, Code
from helper import (
    decoder,
    display_game_board,
    encoder,
    int_input,
    is_draw,
    is_won,
    socket,
)
from setting import HOST, PORT


class Turn:
    def __init__(
        self, server: socket, char: list[str], board_position: list[str]
    ) -> None:
        self.board_position = board_position
        self.server = server
        self.char = char

    def your_turn(self) -> int:
        if is_won(self.board_position, self.char[1]):
            self.server.sendall(encoder({Code.MATCH_CODE: Char.MATCH_LOSS_CHAR}))
            return -1

        print("## Your turn")
        position = int_input("Enter position: ") - 1

        if position not in {0, 1, 2, 3, 4, 5, 6, 7, 8}:
            print("## Position must be in 1-9")
            return self.your_turn()

        if self.board_position[position] != f"{position + 1}":
            print("## Space is filled already")
            return self.your_turn()

        else:
            self.board_position[position] = self.char[0]

            if is_won(self.board_position, self.char[0]):
                self.server.sendall(
                    encoder(
                        {
                            Code.MOVE_CODE: position,
                            Code.MATCH_CODE: Char.MATCH_WIN_CHAR,
                        }
                    )
                )
                return 1

            elif is_draw(self.board_position):
                server.sendall(
                    encoder(
                        {
                            Code.MOVE_CODE: position,
                            Code.MATCH_CODE: Char.MATCH_DRAW_CHAR,
                        }
                    )
                )
                return 5

        self.server.sendall(
            encoder({Code.MOVE_CODE: position, Code.MATCH_CODE: Char.MATCH_NORMAL_CHAR})
        )

        return 0

    def friend_turn(self) -> None:
        print("## Friend turn ...")
        position: int = decoder(self.server.recv(1024))[Code.MOVE_CODE]

        print(f"Friend position {position + 1}")

        self.board_position[position] = self.char[1]


def main_game(server: socket) -> None:
    if decoder(server.recv(1024))[Code.FRIEND_CODE] == 0:
        print("Waiting for friend ...")

        if decoder(server.recv(1024))[Code.FRIEND_CODE] == 1:
            ...

    print("Friend found")

    recived = decoder(server.recv(1024))

    first_turn = True if recived[Code.CHANCE_CODE] else False
    board_position = [f"{i + 1}" for i in range(9)]
    char: list[str] = recived[Code.CHAR_CODE]

    turn = Turn(
        server,
        char,
        board_position,
    )

    if first_turn:
        print("## You are first!")

    else:
        print("## You are second!")

    print(f"Your char {char[0]}")

    while True:
        display_game_board(board_position)
        if first_turn:
            code = turn.your_turn()
            if code != 0:
                if code == 1:
                    display_game_board(board_position)
                    print("## You win ##")

                elif code == -1:
                    print("## You loss ##")

                else:
                    print("## Match draw ##")

                break

        else:
            turn.friend_turn()

            if is_won(board_position, char[1]):
                display_game_board(board_position)

                print()
                print("## You lose")
                server.sendall(encoder({Code.MATCH_CODE: Char.MATCH_LOSS_CHAR}))
                break

            if is_draw(board_position):
                display_game_board(board_position)

                print()
                print("## Match draw ##")
                break

        first_turn = not first_turn


if __name__ == "__main__":
    server = socket(AF_INET, SOCK_STREAM)
    server.connect((HOST, PORT))

    main_game(server)
