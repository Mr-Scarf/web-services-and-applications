import requests

#1. Shuffle the cards and get the deck ID

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
data = response.json()
deck_id = data['deck_id']
#print("Deck ID:", deck_id)


#2. Get the 5 cards from the deck using the deck ID

cards_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(cards_url)
cards_data = response.json()

cards = cards_data['cards']

#3.  Print the cards drawn
print("Cards drawn:")
for card in cards:
    print(f"{card['value']} of {card['suit']}")


#4. Need to do this part - Check if the user has drawn a pair, triple, straight, or all of the same suit and congratulate the user.






