from json import load
from pathlib import Path

url = "https://open-meteo.com/images/country-flags/{}.svg"

with open("country_code.json") as f:
    data: dict[str, str] = load(f)


found = 0
not_found = 0

for k, v in data.items():
    filename = f"flags/{k.lower()}.svg"
    if Path(filename).exists():
        # print(f"{filename} found")
        found += 1

    else:
        # print(f"{filename} not found")
        not_found += 1


print(found, not_found)
