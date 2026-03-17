import requests
import json

host = requests.get("https://internetdb.shodan.io/8.8.8.8").json()

with open("results.json", "w", encoding="utf-8") as file:
    json.dump(host, file, ensure_ascii=False, indent=4)