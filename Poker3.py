__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''
import itertools

rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
suit = ["C", "S", "H", "D"]

def generate_deck():
    deck = []
    for s in suit:
        for r in rank:
            deck.append(s+r)
    return deck

def percentage(top, over):
    return str(round(float(top)/float(over)*100, 2))

def shared_flush(deck):
    deck.remove('CA')
    deck.remove('CK')

    deck.remove('CQ')
    deck.remove('CJ')
    deck.remove('CT')
    deck.remove('SA')
    deck.remove('SK')
    count = 0
    total = 0
    for c1, c2 in itertools.combinations(deck, 2):
        if c1[0] == 'C' and c2[0] == 'C':
            count += 1
        total += 1
    print(str(count) + " out of " + str(total))
    print(percentage(count, total) + "%")

def shared_nuts(deck):
    #royal
    royal = 4
    print("Possible Royal Flushes:\t\t" + str(royal))
    #straight flush K9 Q8 J7 T6 95 84 73 62 5A
    straightflush = 9 * 4
    print("Possible Straight Flushes:\t" + str(straightflush))
    #4 kind
    fourofakind = 0
    for r in rank:
        fourofakind += 52 - 4
    print("Possible Four of a Kind:\t" + str(fourofakind))
    #full
    #13*4(4 choose 3) *  12*6(4 choose 2)
    fullhouse = 13*4*12*6
    print("Possible Full House:\t\t" + str(fullhouse))
    #flush 13 choose 5 * suit
    flush = 1287 * 4 - royal - straightflush
    print("Possible Flushes:\t\t\t"+str(flush))
    #straight
    print(13*4*4*4*4)

def pocket_pair(deck):
    total = 0
    count_pocket_pairs = 0
    for c in itertools.combinations(deck, 2):
        total += 1
        if c[0][1] == c[1][1]:
            count_pocket_pairs += 1
    print("Pocket Pair hands:\t\t\t" + str(count_pocket_pairs))
    print("Total Starting hands:\t\t" + str(total))
    print("Percentage of pocket pair:\t" + percentage(count_pocket_pairs, total) + "%")

shared_flush(generate_deck())
print("############################")
pocket_pair(generate_deck())
print("############################")
shared_nuts(generate_deck())