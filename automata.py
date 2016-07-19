class Player:
    def __init__(self, position, stack):
        self.position = position
        self.stack = stack

import itertools
import random
rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
suit = ["c", "s", "h", "d"]

def generate_deck():
    deck = []
    for s in suit:
        for r in rank:
            deck.append({"rank": r, "suit": s})
    return deck
deck = generate_deck()

def determine(hand, board):
    if hand[0]["suit"] == hand[1]["suit"]:
        suit_count = [c["suit"] for c in board].count(hand[0]["suit"])
        if suit_count >= 3:
            print("flush")
        elif suit_count == 2:
            print("flush draw")
        elif suit_count == 1 and len(board) == 3:
            print("backdoor flush")

    hand.sort(key=lambda a: rank.index(a["rank"]))
    board.sort(key=lambda a: rank.index(a["rank"]))

    values = [b["rank"] for b in board]
    if hand[0]["rank"] in values or hand[1]["rank"] in values:
        res0 = values.count(hand[0]["rank"])
        res1 = values.count(hand[1]["rank"])
        if (res0 == 3 and res1 == 2) or (res0 == 2 and res1 == 3):
            print("Full House")
        if res0 == 3:
            print("Trips")
        if res1 == 3:
            print("Trips")
        if hand[0]["rank"] in values and hand[1]["rank"] in values:
            print("Two Pair")
        if hand[0]["rank"] in values:
            if values.index(hand[0]["rank"]) == 0:
                print("Top")
            elif values.index(hand[0]["rank"]) == 1:
                print("Middle Top")
            elif values.index(hand[0]["rank"]) == 2:
                print("Middle Middle")
            elif values.index(hand[0]["rank"]) == 3:
                print("Middle Bottom")
            elif values.index(hand[0]["rank"]) == 4:
                print("Bottom")
        if hand[1]["rank"] in values:
            if values.index(hand[0]["rank"]) == 0:
                print("Top")
            elif values.index(hand[0]["rank"]) == 1:
                print("Middle Top")
            elif values.index(hand[0]["rank"]) == 2:
                print("Middle Middle")
            elif values.index(hand[0]["rank"]) == 3:
                print("Middle Bottom")
            elif values.index(hand[0]["rank"]) == 4:
                print("Bottom")
    #backdoor straight
    #gutshot
    #double gutted
    #open ended

while True:
    positions = ["BB", "SB", "BTN", "CO", "MP", "UTG"]
    hero_position = positions[random.randrange(len(positions))]

    number_of_players = random.randrange(1, 6)
    players = []
    for n in range(number_of_players):
        if positions[n] != hero_position:
            players.append(Player(positions[n], random.randrange(150, 1200, 5)))
        else:
            players.append(Player(positions[n+1], random.randrange(150, 1500, 5)))

    random.shuffle(deck)
    hand = deck[:2]
    flop = deck[2:5]
    turn = deck[5]
    river = deck[6]

    print("Hand:\t" + hand[0]["rank"] + hand[0]["suit"] + hand[1]["rank"] + hand[1]["suit"])
    #pre flop tree
    if hand[0]["rank"] == hand[1]["rank"]: #pocket pair tree
        print("Position:\t" + hero_position)
        print("".join([p.position + " " + str(p.stack) + "\n" for p in players]))
        preflop_action = input()
        print(hand[0]["rank"]+hand[1]["rank"] + " " +
              hero_position + " [" +
              "".join([p.position + " " + str(p.stack) + " " for p in players]) + "] " +
              preflop_action)
    #print("Flop:\t" + flop[0]["rank"] + flop[0]["suit"] + flop[1]["rank"] + flop[1]["suit"] + flop[2]["rank"] + flop[2]["suit"])
    # print("Action:\t", end="")
    # action = input()
    # print("Logic:\t", end="")
    # logic = input()
    #print("Turn:\t" + turn["rank"] + turn["suit"])
    #print("River:\t" + river["rank"] + river["suit"])

#determine(hand, flop)

'''
preflop tree
    25BB and under - snapshove
    over
        position, action behind, stack size,
'''