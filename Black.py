__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'

rank = ["A", "10", "10", "10", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
suit = ["c", "s", "h", "d"]


def generate_deck():
    deck = []
    for s in suit:
        for r in rank:
            deck.append(r)
    return deck

import random
shoe = []
[shoe.extend(generate_deck()) for i in range(6)]
random.shuffle(shoe)
print(shoe)

while True:
    if len(shoe) < 4:
        break
    dealer = [shoe.pop(), shoe.pop()]
    player = [shoe.pop(), shoe.pop()]

    if "A" not in player:
        total = int(player[0]) + int(player[1])

def decision(player, dealer):
    transPlayer = [9, 10, 11, 12, 13, 14, 15, 16]
    transDealer = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A"]
    chart = [["H", "H", "H", "H"],
             ["H", "H", "H", "H"],
             ["H", "H", "H", "H"],
             ["H", "H", "H", "H"]]