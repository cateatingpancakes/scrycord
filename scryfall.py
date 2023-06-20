import requests

from ratelimit import limits

# Scryfall ratelimit
@limits(calls=10, period=1)
def call(query: str) -> str:

    response = requests.get("https://api.scryfall.com/cards/search?q=" + query)

    if response.status_code == 200:
        return response.json()
    else:
        return None