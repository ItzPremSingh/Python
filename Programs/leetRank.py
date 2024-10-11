from json import loads
from helper import fetch
from sys import argv
from urllib import error


UserID = "Itz_Prem_Singh"
if argv[1::]:
    UserID = argv[1]


try:
    profile = loads(fetch(f"https://leetcode-stats-api.herokuapp.com/{UserID}/"))

except error.URLError as e:  # noqa: F841
    print("Something go went wrong")
    quit()


def precentage(obatined: int, outOf: int) -> str:
    return "(" + str(round((obatined / outOf) * 100, 2)) + "%)"


# Result status
status = profile["status"]
if status != "success":
    print(profile["message"].title())
    quit()

# Total count
totalQuestion: int = profile["totalQuestions"]
totalEasy: int = profile["totalEasy"]
totalMedium: int = profile["totalMedium"]
totalHard: int = profile["totalHard"]

# Solved
totalSolved: int = profile["totalSolved"]
easySolved: int = profile["easySolved"]
mediumSolved: int = profile["mediumSolved"]
hardSolved: int = profile["hardSolved"]

# About user
ranking: int = profile["ranking"]
acceptanceRate: int = profile["acceptanceRate"]
contributionPoints: int = profile["contributionPoints"]
reputation: int = profile["reputation"]

print("User UID:", UserID)
print("Rank:", ranking)

print()

print("Total Solved:", totalSolved, precentage(totalSolved, totalQuestion))

print("Easy:", easySolved, precentage(easySolved, totalEasy))
print("Medium:", mediumSolved, precentage(mediumSolved, totalMedium))
print("Hard:", hardSolved, precentage(hardSolved, totalHard))

print()

print("Acceptance Rate: ", acceptanceRate, "%", sep="")
print("Reputation:", reputation)
print("Points:", contributionPoints)
