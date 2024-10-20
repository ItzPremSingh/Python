from json import loads

from helper import argument, fetch

try:
    from requests import HTTPError

except ModuleNotFoundError:
    from urllib.error import HTTPError

word = argument(__file__)


def foramtter(data) -> None:
    print("Word:", data["word"])

    for meaning in data["meanings"]:
        print(f"\n{meaning['partOfSpeech']}:")
        for definition in meaning["definitions"]:
            print(f"  - {definition['definition']}")
            if "example" in definition:
                print(f"    Example: {definition['example']}\n")

        if meaning["synonyms"]:
            synonyms = ", ".join(meaning["synonyms"])
            print(f"\n    Synonyms: {synonyms}")

        if meaning["antonyms"]:
            antonyms = ", ".join(meaning["antonyms"])
            print(f"\n    Antonyms: {antonyms}")


url = "https://api.dictionaryapi.dev/api/v2/entries/en/%s" % (word)

try:
    loadedJson = loads(fetch(url))

except HTTPError:
    print(f"Meaning not found: {word!r}")
    print("error: Forbidden 404")
    quit()

for data in loads(loadedJson):
    foramtter(data)
