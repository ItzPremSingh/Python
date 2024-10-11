from bs4 import BeautifulSoup

with open("changes.html") as f:
    soup = BeautifulSoup(f, "html.parser")

file = open("outofdir.txt", "a")
for i in soup.find_all("tbody"):
    added = ""
    deleled = ""

    details = i.find_all("tr")
    for j in details:
        detail = j.find_all("td")
        chapter = detail[0].text
        if len(detail) == 2:
            deleled = detail[1].text
        if len(detail) == 3:
            added = detail[2].text

    file.write(f"{chapter}\n{deleled}\n{added}\n")
