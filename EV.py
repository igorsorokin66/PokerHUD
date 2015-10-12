import itertools

def compare(l1, l2):
    print(l1)
    print(l2)

rank = [2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K", "A"]
suit = ["H", "D", "S", "C"]
deck = []
for i in itertools.product(rank, suit):
    deck.append(i)

#regular EV calculator - got it in with +ev
'''
hand0 = [('K', 'H'), ('Q', 'H')]
deck.remove(hand0[0])
deck.remove(hand0[1])
hand1 = [(2, 'D'), (2, 'S')]
deck.remove(hand1[0])
deck.remove(hand1[1])

board = [(2, 'C'), ('J', 'H'), ('T', 'H')]
deck.remove(board[0])
deck.remove(board[1])
deck.remove(board[2])

for turn, river in itertools.permutations(deck, 2):
    compare(hand0 + board + list(turn + river), hand1 + board + list(turn + river))
'''
#######
#what are you beating
hand0 = [('K', 'H'), ('Q', 'H')]
deck.remove(hand0[0])
deck.remove(hand0[1])
board = [('J', 'C'), (2, 'H'), (3, 'H')]
deck.remove(board[0])
deck.remove(board[1])
deck.remove(board[2])

for card1, card2 in itertools.permutations(deck, 2):
    hand1 = [card1, card2]
    deck.remove(hand1[0])
    deck.remove(hand1[1])
    for turn, river in itertools.permutations(deck, 2):
        compare(hand0 + board + list(turn + river), hand1 + board + list(turn + river))
    deck.append(hand1[0])
    deck.append(hand1[1])