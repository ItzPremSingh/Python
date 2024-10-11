from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_website_details(url):
    try:
        with urlopen(url) as response:
            soup = BeautifulSoup(response.read(), "html.parser")
            title = soup.title.string.strip() if soup.title else None
            description_tag = soup.find("meta", attrs={"name": "description"})
            description = (
                description_tag["content"].strip() if description_tag else None
            )
            keywords_tag = soup.find("meta", attrs={"name": "keywords"})
            keywords = keywords_tag["content"].strip() if keywords_tag else None
            favicon_tag = soup.find("link", rel="icon")
            favicon = favicon_tag["href"] if favicon_tag else None
            return {
                "title": title,
                "description": description,
                "keywords": keywords,
                "favicon": favicon,
            }
    except Exception as e:
        print("An error occurred:", e)
        return None


# Example usage:
website_url = "https://www.example.com"
website_details = get_website_details(website_url)
if website_details:
    print("Title:", website_details["title"])
    print("Description:", website_details["description"])
    print("Keywords:", website_details["keywords"])
    print("Favicon URL:", website_details["favicon"])
else:
    print("Failed to retrieve website details.")
