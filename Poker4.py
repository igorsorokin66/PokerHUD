__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''

rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
suit = ["C", "S", "H", "D"]

def generate_deck():
    import random
    deck = ["" for i in range(1, 53)]
    avail = [i for i in range(0, 52)]
    for r in rank:
        for s in suit:
            randNum = random.sample(avail, 1)
            avail.remove(randNum[0])
            deck[randNum[0]] = r + s
    return deck

class Table:
    players = []
    pot = 0
    preflop = []
    flop = []
    turn = []
    river = []
    def __init__(self, players):
        self.players = players

    def bet(self, position, amount, turn):
        self.pot += amount
        if turn == "preflop":
            self.preflop.append({"position": position, "amount": amount})
        elif turn == "flop":
            self.flop.append({"position": position, "amount": amount})
        elif turn == "turn":
            self.turn.append({"position": position, "amount": amount})
        elif turn == "river":
            self.river.append({"position": position, "amount": amount})

def preflop(player, table, min_call):
    cards = player.cards
    if cards[0][1] == cards[1][1]:
        suited = True
    else:
        suited = False
    if cards[0][0] == cards[1][0]:
        pocketpair = True
    else:
        pocketpair = False

    if pocketpair:
        if rank.index(cards[0][0]) < 4: #AA KK QQ JJ
            if min_call >= 15:
                return min_call * 2
            else:
                return 15
        elif rank.index(cards[0][0]) < 8:#TT 99 88 77
            return 15
        else:                           #66 55 44 33 22
            if min_call <= 15:
                return min_call

    if cards[0][0] == "A" or cards[1][0] == "A":#AK AQ AJ AT
        o = ["K", "Q", "J", "T"]
        if cards[0][0] in o or cards[1][0] in o:
            return 5

    if cards[0][0] == "K" or cards[1][0] == "K":#KQ KJ KT
        o = ["Q", "J", "T"]
        if cards[0][0] in o or cards[1][0] in o:
            return 5

    if cards[0][0] == "Q" or cards[1][0] == "Q":#QJ QT
        o = ["J", "T"]
        if cards[0][0] in o or cards[1][0] in o:
            return 5

    if cards[0][0] == "J" or cards[1][0] == "J":#JT
        o = ["T"]
        if cards[0][0] in o or cards[1][0] in o:
            print(cards)
            return

    #suited connectors T9 98 87 76 65 54 43 32 (missing A2)
    if abs(rank.index(cards[0][0])-rank.index(cards[1][0])) == 1 and suited:
        return

    if player.position == "SB":
        return 2
    elif player.position == "BB":
        return 5

class Player:
    def __init__(self, id, stack, position, cards):
        self.id = id
        self.stack = stack
        self.position = position
        self.cards = cards

p1 = Player(1, 250, "D", None)
p2 = Player(2, 250, "SB", None)
p3 = Player(3, 250, "BB", None)
p4 = Player(4, 250, "UTG", None)
p5 = Player(5, 250, "EP", None)
p6 = Player(6, 250, "LP", None)
players = [p1, p2, p3, p4, p5, p6]
positions = ["D", "SB", "BB", "UTG", "EP", "LP"]
action = 3 #player4
for i in range(50):
    deck = generate_deck()
    table = Table([p1, p2, p3, p4, p5, p6])
    i = 0
    for player in players:#deal cards
        player.cards = [deck[i], deck[i+1]]
        i += 2

    min_call = 5
    preflop_action = True
    while preflop_action:
        result = preflop(players[action], table, min_call)

        if action + 1 > len(players):
            action = 0
        else:
            action += 1

    for player in players:#move button
        p = positions.index(player.position)
        if p == 0:
            player.position = "LP"
        else:
            player.position = positions[p-1]