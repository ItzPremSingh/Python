from json import loads

from helper import fetch

api = "hp4YIynh744M5mAePBvqzA==XVBd1dEZqukTGtSV"

api_url = "https://api.api-ninjas.com/v1/facts?limit=1"

jsonData = loads(fetch(api_url, headers={"X-Api-Key": api}))
fact = jsonData[0]["fact"]

print(fact)
