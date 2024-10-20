from urllib.request import Request, urlopen
from sys import argv


def direction(windDir: str) -> str:
    windDirLen = len(windDir)
    if windDirLen > 3 or not windDir:
        return "Unknown"

    windDir = windDir.lower()
    newWindDir = ""

    allDir: dict = {
        "e": "east",
        "w": "west",
        "n": "north",
        "s": "south",
    }

    first = True

    for oneWindDir in windDir:
        if oneWindDir in allDir:
            extractedDir = allDir[oneWindDir]

            if first:
                extractedDir = extractedDir.title()
                first = False

            newWindDir += extractedDir

            if windDirLen == 3:
                newWindDir += "-"
                windDirLen = None

        else:
            return "Unknown"

    return newWindDir


uvColor = {
    0: (28, "Very Low, Fully Heathy"),
    1: (28, "Low, Heathy"),
    2: (28, "Low, Heathy"),
    3: (184, "Moderate, Lesser Risk"),
    4: (184, "Moderate, Lesser Risk"),
    5: (184, "Moderate, Lesser Risk"),
    6: (208, "High, Risk"),
    7: (208, "High, Risk"),
    8: (196, "Very High, Higher Risk"),
    9: (196, "Very High, Higher Risk"),
    10: (196, "Very High, Higher Risk"),
    11: (57, "Extreme, Danger"),
}


def colorText(num: int):
    index = 11 if num > 11 else num
    color, text = uvColor[index]

    return f"\33[48;5;{color}m{num}\33[m {text}"


def month(index: int) -> str:
    __month: dict[int, str] = {
        1: "January",
        2: "February",
        3: "Match",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    return __month.get(index, "Unknown")


def fetch(url: str, headers={}) -> str:
    request = Request(url, headers=headers)
    response = urlopen(request)
    return response.read().decode()


def agent():
    return "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"


def argument(fileName: str) -> str:
    if argv[1::]:
        return argv[1]

    else:
        print(f"Usage: python {fileName.split('/')[-1]} __argument__")
        quit()
