__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''


rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
suit = ["s", "h", "c", "d"]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

def printCards(cards):
    for card in cards:
        print(card.rank + card.suit + " ", end="")
    print()

def shuffle():
    import random
    deck = ["" for i in range(1, 53)]
    avail = [i for i in range(0, 52)]
    for r in rank:
        for s in suit:
            randNum = random.sample(avail, 1)
            avail.remove(randNum[0])
            deck[randNum[0]] = Card(r, s)
    return deck

deck = shuffle()
printCards(deck)
flop = deck[:5]
deck = deck[5:]
printCards(deck)

c = 0
import itertools
for i in itertools.combinations(deck, 2):#brute force nuts engine
    #printCards(i)
    c += 1
print(c)

hand = deck[:2]#efficent
if hand[0].suit == hand[1].suit # and count flush cards on the flop
    flush_flag = True

