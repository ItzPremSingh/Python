from json import loads
from urllib.request import urlopen


def formatter(joke: dict):
    print("Type:", joke["type"])
    print("Setup:", joke["setup"])
    print("Punchline:", joke["punchline"])
    print("\n")


AllTypeOfJoke: list = ["/random_joke", "/random_ten", "/jokes/random", "/jokes/ten"]

url: str = f"https://official-joke-api.appspot.com/{AllTypeOfJoke[0]}"

jsonDict = loads(
    urlopen(
        url,
    )
    .read()
    .decode()
)

if type(jsonDict) is list:
    for data in jsonDict:
        formatter(data)

else:
    formatter(jsonDict)
