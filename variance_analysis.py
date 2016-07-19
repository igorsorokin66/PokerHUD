__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''
import itertools

rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
suit = ["c", "s", "h", "d"]


def generate_deck():
    deck = []
    for s in suit:
        for r in rank:
            deck.append({"rank": r, "suit": s})
    return deck

deck = generate_deck()

total_count = 0
all_hands = {}
for card1, card2 in itertools.combinations(deck, 2):
    total_count += 1
    if rank.index(card2["rank"]) < rank.index(card1["rank"]):
        card2, card1 = card1, card2
    if card1["suit"] == card2["suit"]:
        hand = card1["rank"] + card2["rank"] + "s"
    else:
        hand = card1["rank"] + card2["rank"] + "o"
    if hand in all_hands:
        all_hands[hand] += 1
    else:
        all_hands[hand] = 1

print(all_hands)
suited_connectors = 0
suited_aces = 0
suited_kings = 0
pocket_pairs = 0
for hand in all_hands:
    if hand in ["KQs", "QJs", "JTs", "T9s", "98s", "87s", "76s", "65s", "54s", "43s", "32s"]:
        suited_connectors += all_hands[hand]
        #["T8s", "97s", "86s", "75s", "64s", "53s"]
        #["KJ", KT]
    if hand in ["AJs", "ATs", "A9s", "A8s", "A7s", "A6s", "A5s", "A4s", "A3s", "A2s"]:
        suited_aces += all_hands[hand]
    if hand in ["K9s", "K8s", "K7s", "K6s", "K5s", "K4s", "K3s", "K2s"]:
        suited_kings += all_hands[hand]
    if hand in ["AAo", "KKo", "QQo", "JJo", "TTo", "99o", "88o", "77o", "66o", "55o", "44o", "33o", "22o"]:
        pocket_pairs += all_hands[hand]

print("Total\t\t" + str(total_count))
print("SCs\t\t\t" + str(suited_connectors))
print("Suited Aces\t" + str(suited_aces))
print("Suited Kings" + str(suited_kings))
print("Pairs\t\t" + str(pocket_pairs))