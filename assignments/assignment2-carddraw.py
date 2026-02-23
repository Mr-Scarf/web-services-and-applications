import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
page = requests.get(url)
data = page.json()
deck_id = data['deck_id']

print("Deck ID:", deck_id)

#Get the cards - next step

url = f"https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=2"


