from urllib.request import urlopen


url = "https://geocoding-api.open-meteo.com/v1/search?name=Ghaziabad&count=10&language=en&format=json"

with urlopen(url) as r:
    print(r.read().decode())