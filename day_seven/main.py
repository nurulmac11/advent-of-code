from collections import defaultdict, OrderedDict
import functools

file_path = "test_input.txt"
file_path = "input.txt"

# card_13 = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
card_13 = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}


def compare_deck(item1, item2):
    for i in range(len(item1)):
        c1 = item1[i]
        c2 = item2[i]
        if card_13[c1] < card_13[c2]:
            return -1
        elif card_13[c1] > card_13[c2]:
            return 1
        else:
            continue

deck_points = {
    'fiveofakind': 7,
    'fourofakind': 6,
    'fullhouse': 5,
    'threeofakind': 4,
    'twopair': 3,
    'onepair': 2,
    'highcard': 1
}
deck_mapper = {
    '5': 'fiveofakind',
    '4-1': 'fourofakind',
    '3-2': 'fullhouse',
    '3-1-1': 'threeofakind',
    '2-2-1': 'twopair',
    '2-1-1-1': 'onepair',
    '1-1-1-1-1': 'highcard'
}

def parse_file(file_path):
    data = {'Time': [], 'Distance': []}
    players = []
    with open(file_path, 'r') as file:
        for line in file:
            hand, bid = line.strip().split(' ')
            players.append([hand, bid])
    return players

def analyze_cards(cards):
    global deck_mapper
    card_dict = defaultdict(int)
    joker_count = 0
    wo_joker_dict = defaultdict(int)
    for c in cards:
        if c == 'J':
            joker_count += 1
        else:
            wo_joker_dict[c] += 1
        card_dict[c] += 1

    print(card_dict)
    counts = []
    wo_joker_counts = []
    for k, v in card_dict.items():
        counts.append(str(v))
    for k, v in wo_joker_dict.items():
        wo_joker_counts.append(str(v))
    if wo_joker_counts:
        wo_joker_counts.sort(reverse=True)
        wo_joker_counts[0] = str(int(wo_joker_counts[0]) + joker_count)
        joker_hashed = "-".join(sorted(wo_joker_counts, reverse=True))
        return deck_mapper[joker_hashed]
    # print(counts, wo_joker_counts)
    hashed = "-".join(sorted(counts, reverse=True))
    # print(counts, hashed, deck_mapper[hashed])
    return deck_mapper[hashed]


player_list = parse_file(file_path)
result = 1

deck_list = OrderedDict()
for k, v in deck_points.items():
    deck_list[k] = []

result = 0
deck_bid = {}
for cards, bid in player_list:
    deck_name = analyze_cards(cards)
    deck_list[deck_name].append(cards)
    deck_bid[cards] = int(bid)

print(deck_list)
for k in deck_list:
    result = sorted(deck_list[k], key=functools.cmp_to_key(compare_deck), reverse=True)
    deck_list[k] = result
rank = len(player_list)
result = 0
print(deck_list)
for set_name, decks in deck_list.items():
    for deck in decks:
        print(deck, rank)
        result += rank * deck_bid[deck]
        rank -= 1

print(result)
