from urllib.request import urlopen

from setting import NEW_NAME

url = f"https://geocode.maps.co/reverse?lat=28.669080&lon=77.430410&api_key={NEW_NAME}"

with urlopen(url) as response:
    data = response.read().decode()
    print(data)
