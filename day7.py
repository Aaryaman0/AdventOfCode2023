h = {'five_kind': [], 'four_kind': [], 'full_house': [], 'three_kind' : [], 
         'two_pair': [], 'one_pair': [], 'high_card': []}

# Problem 1
# ordering = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5,
#             '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}

# Problem 2
ordering = {'A': 12, 'K': 11, 'Q': 10, 'J': 0, 'T': 9, '9': 8, '8': 7, '7': 6,
            '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
arr = []
from collections import Counter

def get_value(card):
    char = card[0]
    count = 0
    factor = (13 ** 5)
    for c in char:
        count += factor * ordering[c]
        factor /= 13
    return count

# Problem 1

# def check_card(card):
#     char = card[0]
#     value = card[1]
#     counter = Counter(char)
#     if len(counter.keys()) == 1:
#         h['five_kind'].append(card)
#     elif len(counter.keys()) == 2:
#         if max(counter.values()) == 4:
#             h['four_kind'].append(card)
#         else:
#             h['full_house'].append(card)
#     elif len(counter.keys()) == 3:
#         if max(counter.values()) == 3:
#             h['three_kind'].append(card)
#         else:
#             h['two_pair'].append(card)
#     elif len(counter.keys()) == 4:
#         h['one_pair'].append(card)
#     else:
#         h['high_card'].append(card)

# Problem 2

def check_card(card):
    char = card[0]
    value = card[1]
    counter = Counter(char)
    maxi = 0
    if 'J' in counter:
        extra = counter['J']
        del counter['J']
        if counter == {}:
            counter['J'] = 5
            maxi = 5
        else:
            maxi = max(counter.values()) + extra
    else:
        maxi = max(counter.values())
    if len(counter.keys()) == 1:
        h['five_kind'].append(card)
    elif len(counter.keys()) == 2:
        if maxi == 4:
            h['four_kind'].append(card)
        else:
            h['full_house'].append(card)
    elif len(counter.keys()) == 3:
        if maxi == 3:
            h['three_kind'].append(card)
        else:
            h['two_pair'].append(card)
    elif len(counter.keys()) == 4:
        h['one_pair'].append(card)
    else:
        h['high_card'].append(card)

with open('day7.txt', 'r') as file:
    final = 0
    arr = []
    for line in file:
        arr.append(line[:-1].split(' '))
    l = len(arr)
    for card in arr:
        check_card(card)
    for key in h.keys():
        print(key)
        h[key] = sorted(h[key], key=get_value, reverse=True)
        for card in h[key]:
            print(card, get_value(card))
            final += l * int(card[1])
            l -=1 
    print(final)

    