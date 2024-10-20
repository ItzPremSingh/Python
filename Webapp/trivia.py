from html import unescape
from json import loads
from random import shuffle

from helper import fetch

url = "https://opentdb.com/api.php?amount=10&category=19&type=multiple"

jsonDict = loads(fetch(url))


def detail(__dict) -> None:
    _ = __dict.get
    print("Category:", _("category"))
    print("Type:", _("type"))
    print("Difficulty:", _("difficulty"))
    print("Question:", unescape(_("question")))


def mcq(__dict: dict) -> bool:
    detail(__dict)
    _ = __dict.get
    correctAnswer = _("correct_answer")
    options: list = [
        correctAnswer,
        *_("incorrect_answers", ""),
    ]

    shuffle(options)
    print("Options:")
    for index, option in enumerate(options):
        print(f"  {index + 1}.", option)

    userAnswer: int = int(input("Enter index: ")) - 1
    print()
    if options[userAnswer] == correctAnswer:
        print("Correct Answer")
        return True

    else:
        print(f"Wrong Answer! correct {correctAnswer}")
        return False


right = 0
wrong = 0

for quest in jsonDict["results"]:
    print(f"Total right: {right}, wrong: {wrong}\n")
    answer = mcq(quest)
    if answer:
        right = +1
    else:
        wrong += 1
