import json

with open('tst.json', 'r') as file:
    data = json.load(file)

cards_with_id = data['cards']

def third_card(a, b, c):
    return [p1 if p1 == p2 else 6 - p1 - p2 for p1, p2, p3 in zip(a, b, c)]

cards = []

for card in cards_with_id:
    new_card = {key: value for key, value in card.items() if key != 'id'}
    cards.append(new_card)

third_cards = []

for i in range(len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)):
            third_cards.append(third_card(cards[i].values(), cards[j].values(), cards[k].values()))

print(*cards)
for card in third_cards:
    print(card)
