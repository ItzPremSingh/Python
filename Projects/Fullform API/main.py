from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

BASE_URL = "https://fullforms.com/"


def get_popularity(val: str) -> int:
    """
    Convert string popularity value to integer

    The string value is in the format of "width:100%;"
    """

    return int(val[6:-1])


def get_fullform(text: str) -> dict[str, object]:
    """
    Get fullform information of the input text

    Returns:
        dict: Contains fullform information
    """

    data: dict[str, object] = {}
    isotope_list: list[dict[str, object]] = []
    similar_terms: list[dict[str, str]] = []

    with urlopen(
        Request(
            BASE_URL + text.upper(),
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0"
            },
        )
    ) as response:
        content = response.read().decode("utf-8")

    soup = BeautifulSoup(content, "html.parser")

    arial = soup.findAll("td", {"class": "arial"})

    if len(arial) == 0:
        f = soup.find("div", {"class": "content-wrap"})
        a = f.find("div", {"class": "content"})  # type: ignore
        d = a.find("div", {"class": "addnew"})  # type: ignore

        data["match_found"] = False
        data["suggestion"] = [i.text for i in d.findAll("a")]  # type: ignore
        return data

    main_fullform: str = arial[0].find("strong").text
    main_category: tuple[str, str] = tuple(
        i.text.strip() for i in arial[1].findAll("strong")
    )
    main_region: str = arial[2].find("strong").text.strip()

    popularity = soup.find("div", {"class": "pop-bar"}).get("style")  # type: ignore
    main_popularity_percent: int = get_popularity(popularity)  # type: ignore

    isotope = soup.find("table", {"id": "isotope"}).findAll("tr")  # type: ignore

    for i in isotope:
        td = i.findAll("td")

        percent: int = get_popularity(
            td[0]
            .find("div", {"class": "t-pop"})
            .find("div", {"class": "popularity"})
            .find("div", {"class": "pop-bar"})
            .get("style")
        )
        country_region: str = td[1].find("img").get("title")
        shortform: str = td[2].find("a").text
        fullform: str = td[3].find("a").text.strip()
        category = td[4].find("div", {"class": "cat-wrap"})

        category1 = category.find("div", {"class": "category1"}).text
        category2 = category.find("div", {"class": "category2"}).text.strip()

        isotope_dict = {}

        isotope_dict["shortform"] = shortform
        isotope_dict["fullform"] = fullform
        isotope_dict["popularity"] = percent
        isotope_dict["region"] = country_region
        isotope_dict["category"] = (category1, category2)

        isotope_list.append(isotope_dict)

    for i in soup.find("div", {"class": "similar-terms"}).find("ul").findAll("li"):  # type: ignore
        spans = i.findAll("span")
        similar_terms.append(
            {"shortform": spans[0].text[:-3], "fullform": spans[1].text}
        )

    abbreviations: list[str] = [
        i.find("a").text
        for i in soup.find("div", {"class": "nearby-terms"}).find("ul").findAll("li")  # type: ignore
    ]

    data["match_found"] = True
    data["fullform"] = main_fullform
    data["category"] = main_category
    data["region"] = main_region
    data["popularity"] = main_popularity_percent
    data["isotope"] = isotope_list
    data["similar_terms"] = similar_terms
    data["abbreviations"] = abbreviations

    return data
