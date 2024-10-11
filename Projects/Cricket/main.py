from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


# with urlopen(
#     Request(
#         "https://www.cricbuzz.com/cricket-match/live-scores",
#         headers={"User-Agent": user_agent},
#     )
# ) as response:
#     data = response.read().decode("utf-8")


with open("cricket.html") as f:
    data = f.read()

soup = BeautifulSoup(data, "html.parser")

match_list = soup.find("div", {"class": "cb-mtch-lst"})
h3 = match_list.find("h3", {"class": "cb-lv-scr-mtch-hdr"})
a = h3.find("a", {"class": "text-hvr-underline"})

teams = a.get("title").split(" vs ")

text_gray = soup.find("span", {"class": "text-gray"})
div_gray = soup.find("div", {"class": "text-gray"})

print(div_gray.text)

div_gray_span = div_gray.find_all("span")

print(div_gray_span[0].text, div_gray_span[-1].text)
