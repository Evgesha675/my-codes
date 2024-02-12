import json

with open('tst.json', 'r') as file:
    data = json.load(file)

cards_with_id = data['cards']

def third_card(a, b):
    result = {
        'color': list(a)[0] if list(a)[0] == list(b)[0] else 6 - list(a)[0] - list(b)[0],
        'shape': list(a)[1] if list(a)[1] == list(b)[1] else 6 - list(a)[1] - list(b)[1],
        'fill': list(a)[2] if list(a)[2] == list(b)[2] else 6 - list(a)[2] - list(b)[2],
        'count': list(a)[3] if list(a)[3] == list(b)[3] else 6 - list(a)[3] - list(b)[3]
    }
    return result


cards = []

for card in cards_with_id:
    new_card = {key: value for key, value in card.items() if key != 'id'}
    cards.append(new_card)


print("Карты из JSON и третья карта:")
for i in range(len(cards) - 1):
    for j in range(i + 1, len(cards)):
        print(cards[i])
        print(cards[j])
        print(third_card(cards[i].values(), cards[j].values()))
        print()
