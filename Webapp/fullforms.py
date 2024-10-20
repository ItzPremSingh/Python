try:
    from bs4 import BeautifulSoup

except ModuleNotFoundError:
    print("Please install bs4 module")
    quit()

from helper import agent, argument, fetch


def fullform(shortForm: str) -> dict:
    fullformDict: dict = {"match_found": False}
    fullformDict["short_form"] = shortForm

    url = f"https://fullforms.com/{shortForm}"
    header = {"User-Agent": agent()}
    htmlText = fetch(url, headers=header)

    soup = BeautifulSoup(htmlText, "html.parser")
    fullForm = soup.find(class_="blue").text

    if shortForm == fullForm:
        suggestion = [
            data.text for data in soup.find(class_="notfound-suggestions").findAll("a")
        ]
        fullformDict.setdefault("suggestions", suggestion)
        return fullformDict

    else:
        category = soup.findAll("td")[5].text
        fullformDict["match_found"] = True
        fullformDict.setdefault("best_match", {fullForm: category})
        extraForm: dict = {}
        shortForms = soup.findAll("td")

        for extraFullform in shortForms:
            if moreTerm := extraFullform.find(class_="more-term"):
                moreCat = extraFullform.find(class_="more-cat")

                extraForm.setdefault(moreTerm.text, moreCat.text)

        fullformDict.setdefault("extra_match", extraForm)

        return fullformDict


def dictFormatter(_dict: dict, sep=": ", start="   -") -> None:
    for key, value in _dict.items():
        print(f"{start} {key}{sep}{value}")


word = argument(__file__)


fullformDict = fullform(word)

if fullformDict["match_found"]:
    print("Match found:", "Yes\n")

    bestMatch = fullformDict["best_match"]
    print("Best match")
    dictFormatter(bestMatch)

    extraMatch = fullformDict["extra_match"]
    if extraMatch:
        print()
        print("Extra match")
        dictFormatter(extraMatch)

else:
    print("Match found:", "No")
    if suggest := fullformDict["suggestions"]:
        print("Suggestion:", ", ".join(suggest))
