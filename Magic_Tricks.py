__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
import random

resultsHH = []
for i in range(10000):
    last_two = ""
    while not (last_two[-2:] == "HH"):
        if random.randrange(2) == 1:
            if last_two[-1:] == "T":
                last_two = "T"
            else:
                last_two += "H"
        else:
            last_two += "T"
    resultsHH.append(len(last_two))

resultsHT = []
for i in range(10000):
    last_two = ""
    while not (last_two[-2:] == "HT"):
        if random.randrange(2) == 1:
            if last_two[-1:] == "T":
                last_two = "T"
            else:
                last_two += "H"
        else:
            last_two += "T"
    resultsHT.append(len(last_two))
import statistics
print(statistics.mean(resultsHH))
print(statistics.mean(resultsHT))



def cut_the_deck(deck):
    rand = random.randrange(51)+1
    deck1 = []
    deck1.extend(deck[rand:])
    deck1.extend(deck[:rand])
    return deck1


def riffle_shuffle(deck):
    i = 0
    deck2 = []
    for a in list(reversed(deck[:26])):
        rand = random.randrange(5)+1
        deck2.extend(a.split())
        deck2.extend(deck[26:][i:i+rand])
        i += rand
    return deck2


def thirteen_non_repeating_cards():
    deck = []
    rank1 = ["8", "K", "3", "T", "2", "7", "9", "5", "Q", "4", "A", "6", "J"]
    suit1 = ["c", "d", "s", "h"]
    for s in suit1:
        for r in rank1:
            deck.append(r + s)

    #  cut the deck
    deck1 = cut_the_deck(deck)
    #print(deck)
    #print(deck1)

    # riffle shuffle
    deck2 = riffle_shuffle(deck1)
    print(deck2)
#thirteen_non_repeating_cards()
