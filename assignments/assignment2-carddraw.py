import requests
import json

#1. Shuffle the cards and get the deck ID

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)

if response.status_code != 200:
    print(f"Error fetching cards")
    exit()  # or return, or raise error
data = response.json()
deck_id = data['deck_id']
#print("Deck ID:", deck_id)


#2. Get the 5 cards from the deck using the deck ID

cards_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5" # Draw 5 cards
response = requests.get(cards_url)
if response.status_code != 200:
    print(f"Error fetching cards")
    exit()  # or return, or raise error
cards_data = response.json()

cards = cards_data['cards']

#3.  Print the cards drawn
print("Cards drawn:")
for card in cards:
    print(f"{card['value']} of {card['suit']}")


#4. Check if the user has drawn a pair, triple, straight, or all of the same suit and congratulate the user.

# Reference: ' For the below code on selecting cards how would I : Check if the user has drawn a pair, triple, straight, or all of the same suit
# and congratulate the user? '
# https://chatgpt.com/share/69dbe9d9-0578-832e-bc00-b20a3defe5bd

# Check hand type

values = [card['value'] for card in cards]
suits = [card['suit'] for card in cards]

# Convert face cards to numbers for straight checking
value_map = {
    "ACE": 14,
    "KING": 13,
    "QUEEN": 12,
    "JACK": 11
}

numeric_values = []
for v in values:
    if v.isdigit():
        numeric_values.append(int(v))
    else:
        numeric_values.append(value_map[v])

numeric_values.sort()

# Count occurrences of each value
value_counts = {}
for v in values:
    value_counts[v] = value_counts.get(v, 0) + 1

counts = value_counts.values()

# ---- Check combinations ----

# Pair / Triple
if 3 in counts:
    print("🎉 You got a THREE OF A KIND!")
elif list(counts).count(2) == 2:
    print("🎉 You got TWO PAIRS!")
elif 2 in counts:
    print("🎉 You got a PAIR!")

# Flush (all same suit)
if len(set(suits)) == 1:
    print("🎉 You got a FLUSH (all same suit)!")

# Straight (consecutive values)
is_straight = True
for i in range(len(numeric_values) - 1):
    if numeric_values[i] + 1 != numeric_values[i + 1]:
        is_straight = False
        break

# Special case: A-2-3-4-5 straight
if numeric_values == [2, 3, 4, 5, 14]:
    is_straight = True

if is_straight:
    print("🎉 You got a STRAIGHT!")






