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


def percentage(top, over, sigfig):
    return str(round(float(top)/float(over)*100, sigfig))


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
    print(percentage(count, total, 2) + "%")

def shared_flush_which_beats_yours(deck):
    deck.remove('CA')
    deck.remove('CQ')

    deck.remove('CJ')
    deck.remove('CT')
    deck.remove('C9')
    deck.remove('SA')
    deck.remove('SK')
    count = 0
    total = 0
    for c1, c2 in itertools.combinations(deck, 2):
        if c1[0] == 'C' and c2[0] == 'C':
            if c1[1] == 'K' or c2[1] == 'K':
                count += 1
            total += 1
    print(str(count) + " out of " + str(total))
    print(percentage(count, total, 2) + "%")

def shared_nuts(deck):
    #  royal
    royal = 4
    print("Possible Royal Flushes:\t\t" + str(royal))
    #  straight flush K9 Q8 J7 T6 95 84 73 62 5A
    straightflush = 9 * 4
    print("Possible Straight Flushes:\t" + str(straightflush))
    #  4 kind
    four_of_a_kind = 0
    for r in rank:
        four_of_a_kind += 52 - 4
    print("Possible Four of a Kind:\t" + str(four_of_a_kind))
    #  full
    #  13*4(4 choose 3) *  12*6(4 choose 2)
    fullhouse = 13*4*12*6
    print("Possible Full House:\t\t" + str(fullhouse))
    #  flush 13 choose 5 * suit
    flush = 1287 * 4 - royal - straightflush
    print("Possible Flushes:\t\t\t"+str(flush))
    #  straight
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
    print("Percentage of pocket pair:\t" + percentage(count_pocket_pairs, total, 2) + "%")


def royal_flushes_in_fantasyland(deck):
    number_of_all_fantasyland_draws = 635013559600  # 52 choose 13
    # first 5 cards of the fantasyland is a royal flush
    number_of_remaining_fantasyland_cards = 314457495 # 47 choose 8
    # multiply by 4 for 4 possible royal flushes
    number_of_royal_flushes_in_fantasyland = number_of_remaining_fantasyland_cards * 4
    print(str(number_of_royal_flushes_in_fantasyland) + " out of " + str(number_of_all_fantasyland_draws))
    print(percentage(number_of_royal_flushes_in_fantasyland, number_of_all_fantasyland_draws, 4) + "%")

def four_card_flush_ofc(deck):
    deck.remove("CA")
    deck.remove("CK")
    deck.remove("CQ")
    deck.remove("CJ")
    deck.remove("HA")

    # 314457495 all remaining 8 card possibilities
    # remove 9 flush cards from 47 = 38 remaining
    # 48903492 38 choose 8
    i = 0
    for c in itertools.combinations(deck, 8):
        i += 1
    print(i)

def bad_beat_AA_vs_J7(deck):
    deck.remove("CA")
    deck.remove("HA")
    deck.remove("CJ")
    deck.remove("H7")

    # flop
    deck.remove("CQ")
    deck.remove("HQ")
    deck.remove("D2")

    hit = 0
    total = 0
    for c in itertools.combinations(deck, 2):
        total += 1
        if ("7" in c[0] and "7" in c[1]) or ("J" in c[0] and "J" in c[1]):
            hit += 1
    print("Total: " + str(total))
    print("Hit: " + str(hit))

def worst_bad_beat(deck):
    deck.remove("CA")
    deck.remove("HA")
    deck.remove("CK")
    deck.remove("HK")

    # flop
    deck.remove("DA")
    deck.remove("SA")
    deck.remove("D2")

    hit = 0
    total = 0
    for c in itertools.combinations(deck, 2):
        total += 1
        if "K" in c[0] and "K" in c[1]:
            hit += 1
    print("Total: " + str(total))
    print("Hit: " + str(hit))

def SF_bad_beat(deck):
    deck.remove("C5")
    deck.remove("C6")
    deck.remove("CA")
    deck.remove("HA")

    # flop
    deck.remove("DA")
    deck.remove("SA")
    deck.remove("C8")

    import Determine
    cards = [Determine.Card('5', 'C'),
             Determine.Card('6', 'C'),
             Determine.Card('8', 'C')]

    hit = 0
    total = 0
    for c in itertools.combinations(deck, 2):
        c1 = Determine.Card(c[0][1], c[0][0])
        c2 = Determine.Card(c[1][1], c[1][0])
        cards.append(c1)
        cards.append(c2)
        rez = Determine.determine_combo(cards)
        cards.remove(c1)
        cards.remove(c2)
        if rez[0] == 9:
            print(rez)
    print("Total: " + str(total))
    print("Hit: " + str(hit))

print("Shared 3 card flush")
shared_flush(generate_deck())
print("############################")
print("Shared 3 card flush")
shared_flush_which_beats_yours(generate_deck())
print("############################")
pocket_pair(generate_deck())
print("############################")
shared_nuts(generate_deck())
print("############################")
royal_flushes_in_fantasyland(generate_deck())
print("############################")
#four_card_flush_ofc(generate_deck())
print("############################")
bad_beat_AA_vs_J7(generate_deck())
print("############################")
worst_bad_beat(generate_deck())
SF_bad_beat(generate_deck())