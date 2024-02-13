import json


color_mapping = {1: 'чёрный', 2: 'белый', 3: 'оранжевый'}
shape_mapping = {1: 'параллелепипед', 2: 'окружность', 3: 'звездочка'}
fill_mapping = {1: 'заполнено', 2: 'пусто', 3: 'заштрихованно'}

with open('tst.json', 'r') as file:
    data = json.load(file)

cards_with_id = data['cards']

def third_card(a, b):
    result = {
        'color': color_mapping[a['color']] if a['color'] == b['color'] else color_mapping[6 - a['color'] - b['color']],
        'shape': shape_mapping[a['shape']] if a['shape'] == b['shape'] else shape_mapping[6 - a['shape'] - b['shape']],
        'fill': fill_mapping[a['fill']] if a['fill'] == b['fill'] else fill_mapping[6 - a['fill'] - b['fill']],
        'count': a['count'] if a['count'] == b['count'] else 6 - a['count'] - b['count']
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
        print('сет', third_card(cards[i], cards[j]))
        print()
