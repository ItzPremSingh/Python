from json import load

with open("data.json") as f:
    data = load(f)

with open("currency_data.json") as f:
    d = load(f)

for c, v in data["conversion_rates"].items():
    if v < 1:
        print(d[c], v)
