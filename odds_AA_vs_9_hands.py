
import random
import itertools
rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
suit = ["H", "D", "S", "C"]

deck = []
for i in itertools.product(rank, suit):
    deck.append(i)

random.shuffle(deck)
print(deck)

deck.remove(('A', 'S'))
deck.remove(('A', 'H'))
print(deck)

total = 100
otherTotal = 100
for i in range(200):
    if random.randrange(100) < 30:
        total += 9
        otherTotal -= 9
    else:
        total -= 1
        otherTotal += 9
print(total)
print(otherTotal)