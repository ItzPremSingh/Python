from datetime import datetime
from json import dump, load
from pathlib import Path
from urllib import error

from bs4 import BeautifulSoup
from helper import fetch

date = datetime.now().strftime("%D")


def jsonBuilder(response, date) -> dict:
    jsonData = {}
    selecter = "border px-2 mb-3 rounded bg-light my-2 text-center"

    soup = BeautifulSoup(response, "html.parser")
    quotes = soup.find(class_=selecter).blockquote.strings
    quote = next(quotes)
    by = next(quotes)

    jsonData.setdefault("date", date)
    jsonData.setdefault("quote", quote)
    jsonData.setdefault("by", by)

    return jsonData


filename = ".quotes.json"
file = Path(filename)

url = "https://www.shabdkosh.com/quote-of-the-day/english-hindi/"
header = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile DuckDuckGo/5 Safari/537.36"
}

try:
    response = fetch(url, headers=header)

except error.URLError:
    if Path(filename).exists():
        with open(filename) as file:
            jsonDict = load(file)
            if not jsonDict["date"] == date:
                print(f'Quote of date: {jsonDict["date"]}\n')

    else:
        quit()

else:
    jsonDict = jsonBuilder(response, date)
    with open(filename, "w") as file:
        dump(jsonDict, file)

    print("Quote saved for offline")


print(f'Todays quote by {jsonDict["by"]!r}.\n')
print(jsonDict["quote"])
