from random import choice, randint, shuffle
from re import search
from argparse import ArgumentParser

parser = ArgumentParser(description="Math game to build fast mind")

parser.add_argument(
    "-start", "-s", type=int, help="Starting range of number (default 1)", default=1
)

parser.add_argument(
    "-end", "-e", type=int, help="Ending range of number (default 10)", default=10
)
parser.add_argument(
    "--operators",
    "--o",
    nargs="*",
    choices=[
        "a",
        "add",
        "s",
        "subtract",
        "m",
        "multiply",
        "d",
        "divide",
    ],
    help="Specify operator(s)-: a or add, s or subtract, m or multiply, d or divide (default ALL)",
    default=["+", "-", "*", "/"],
)

parser.add_argument(
    "--types",
    "--t",
    nargs="*",
    choices=["f", "fill", "b", "bool", "m", "mcq"],
    help="Specify type(s)-: f or fill, b or bool, m or mcq (default ALL)",
    default=["fill", "bool", "mcq"],
)

args = parser.parse_args()


"""
minnum: int = 1
maxnum: int = 10
operator: list = [
    "+",
    "-",
    "*",
    "/",
]

questionType: list = [
    "fill",
    "bool",
    "mcq",
]
"""

minnum = args.start
maxnum = args.end

operator = args.operators
questionType = args.types


def inputBool(string: str = "") -> bool:
    while True:
        inputData: str = input(string)
        if reSearch := search(
            r"^\s*(?P<bool>(true|false|[tf]))\s*$", inputData.lower()
        ):
            _bool = reSearch.group("bool")
            return True if _bool in ("t", "true") else False


def inputInt(string: str = "") -> int:
    while True:
        inputData: str = input(string)
        if reSearch := search(r"^\s*(?P<number>\d+)\s*$", inputData):
            return int(reSearch.group("number"))


def add() -> tuple[int, int]:
    first: int = randint(minnum, maxnum)
    second: int = randint(minnum, maxnum)

    return first, second


def subtract() -> tuple[int, int]:
    first: int = randint(minnum, maxnum)
    second: int = randint(minnum, first)

    return first, second


def multiply() -> tuple[int, int]:
    return add()


def divide() -> tuple[int, int]:
    first, second = add()
    return first * second, first


def fill() -> int:
    answer: int = 0
    symbol: str = choice(operator)
    first: int = 0
    second: int = 0

    if symbol == "+":
        first, second = add()
        answer = first + second

    elif symbol == "-":
        first, second = subtract()
        answer = first - second

    elif symbol == "*":
        first, second = multiply()
        answer = first * second

    elif symbol == "/":
        first, second = divide()
        answer = first // second

    print(first, symbol, second, end=" = ")

    return answer


def bools() -> bool:
    answer: int = 0
    isCorrect = randint(0, 1)

    symbol: str = choice(operator)
    first: int = 0
    second: int = 0

    if symbol == "+":
        first, second = add()
        answer = first + second

    elif symbol == "-":
        first, second = subtract()
        answer = first - second

    elif symbol == "*":
        first, second = multiply()
        answer = first * second

    elif symbol == "/":
        first, second = divide()
        answer = first // second

    if not isCorrect:
        _random = randint(1, 2)
        if _random == 1:
            second += randint(1, 5)

        else:
            answer -= randint(1, 5)

    print(first, symbol, second, "=", answer)

    return True if isCorrect else False


def mcq() -> list:
    options: list = []
    answer: int = fill()
    print("?\n")

    options.append(answer)
    total = 1

    while total <= 3:
        _random = randint(1, 2)
        if _random == 1:
            answer += randint(1, 5)

        else:
            answer -= randint(1, 5)

        if answer in options:
            continue

        options.append(answer)
        total += 1

    return options


correct: int = 0
wrong: int = 0
total: int = 0
maxQuestion: int = 10
questionIndex: int = 1
isUnlimited: bool = False


while True:
    if maxQuestion < total and not isUnlimited:
        break

    _random = choice(questionType)
    print(f"Question: [{questionIndex}", end="")
    if not isUnlimited:
        print(f"/{maxQuestion}]", end=" ")

    if _random == "fill":
        print("[Fill ups]")
        realanswer: int = fill()
        useranswer: int = inputInt()

        if realanswer == useranswer:
            correct += 1

        else:
            # print("wrong", realanswer, "\n")
            wrong += 1

    elif _random == "bool":
        print("[True or False]")
        realbool: bool = bools()
        userbool: bool = inputBool("t or f? ")

        if realbool == userbool:
            # print("correct\n")
            correct += 1

        else:
            # print("wrong\n")
            wrong += 1

    elif _random == "mcq":
        print("[MCQ]")
        option: list = mcq()
        answer: int = option[0]
        shuffle(option)
        for index, number in enumerate(option):
            print(index + 1, ". ", number, sep="")

        while True:
            index: int = inputInt("Enter index [1-4]: ") - 1
            if index in range(4):
                break

        if option[index] == answer:
            # print("correct\n")
            correct += 1

        else:
            # print("wrong\n")
            wrong += 1

    total += 1
    questionIndex += 1
    print("\n")

print("correct:", correct)
print("wrong:", wrong)
