from helper import fetch
from json import loads

text = fetch("https://api.ipify.org/?format=json")
loaded = loads(text)
ip = loaded["ip"]
print("Your IP address:", ip)


def formatter(__dict: dict):
    get = __dict.get
    print("City:", get("city"))
    print("Region:", get("region"))
    print("Country:", get("country"))
    print("Location:", get("loc"))
    print("Organization:", get("org"))
    print("Postal:", get("postal"))
    print("Timezone:", get("timezone"))


ipdata = loads(fetch(f"https://ipinfo.io/{ip}/geo"))

formatter(ipdata)
