__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''


rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
suit = ["S", "H", "C", "D"]

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

def order_by_rank(cards):
    rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    cards_dict_by_rank_index = {card: rank.index(card) for card in cards}
    cards_sorted_by_rank_index = sorted(cards_dict_by_rank_index, key=cards_dict_by_rank_index.get)
    return cards_sorted_by_rank_index

def get_kickers(cards, exclusions, number_of_kickers):
    kickers = order_by_rank(list(set(cards).difference(set(exclusions))))
    return kickers[:number_of_kickers]

def determine_combo(cards):
    suit = ["C", "S", "H", "D"]
    suit_count = dict(zip(suit, [[] for i in range(0, 4)]))
    rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    rank_count = {}
    flush_flag = False
    for card in cards:
        suit_count[card.suit].append(card)
        if card.rank not in rank_count.keys():
            rank_count[card.rank] = 1
        else:
            rank_count[card.rank] += 1
        if len(suit_count[card.suit]) == 5:
            flush_flag = True
            flush_suit = card.suit

    rank_count_ordered_by_rank = order_by_rank(rank_count.keys())
    Ato5 = rank[9:13] + [rank[0]]#Exception A,2,3,4,5 A TO 6 ERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR
    for i in range(0, 9):
        if set(rank[0+i:5+i]).issubset(set(rank_count_ordered_by_rank)):
            if flush_flag:
                if i is 0:
                    return [10, rank[0+i:5+i]]#Royal Flush
                else:
                    return [9, rank[0+i:5+i]]#Straight Flush
            else:
                return [5, rank[0+i:5+i]]#Straight
        if i == 8 and set(Ato5).issubset(set(rank_count_ordered_by_rank)):
            if flush_flag:
                return [9, Ato5]#Steel Wheel
            else:
                return [5, Ato5]#Wheel

    #Flush
    if flush_flag:
        flush_cards = [card.rank for card in suit_count[flush_suit]]
        flush_cards_ordered_by_rank = order_by_rank(flush_cards)
        return [6, flush_cards_ordered_by_rank]

    count_to_rank = {}
    for k, v in rank_count.items():
        count_to_rank[v] = count_to_rank.get(v, [])
        count_to_rank[v].append(k)
    for k in count_to_rank.keys():
        count_to_rank[k] = order_by_rank(count_to_rank[k])
    count_to_rank_sorted = []
    for k in sorted(count_to_rank, reverse=True):
        count_to_rank_sorted.append(count_to_rank[k])

    #Four of a Kind
    if 4 in count_to_rank.keys():
        four_of_a_kind = [count_to_rank_sorted[0][0]] * 4
        kicker = get_kickers(rank_count, count_to_rank_sorted[0], 1)
        return [8, four_of_a_kind + kicker]
    #Full House
    elif 3 in count_to_rank.keys() and (2 in count_to_rank.keys() or len(count_to_rank[3]) > 1):
        if len(count_to_rank[3]) > 1:
            return [7, [count_to_rank_sorted[0][0]] * 3 + [count_to_rank_sorted[0][1]] * 2]
        else:
            return [7, [count_to_rank_sorted[0][0]] * 3 + [count_to_rank_sorted[1][0]] * 2]
    #Three of a Kind
    elif 3 in count_to_rank.keys():
        three_of_a_kind = [count_to_rank_sorted[0][0]] * 3
        return [4, three_of_a_kind + [count_to_rank_sorted[1][0], count_to_rank_sorted[1][1]]]
    #Two Pair
    elif 2 in count_to_rank.keys() and len(count_to_rank_sorted[0]) > 1:
        first_pair = [count_to_rank_sorted[0][0]] * 2
        second_pair = [count_to_rank_sorted[0][1]] * 2
        kicker = get_kickers(rank_count, count_to_rank_sorted[0], 1)
        return [3, first_pair + second_pair + kicker]
    #One Pair
    elif 2 in count_to_rank.keys():
        return [2, [count_to_rank_sorted[0][0], count_to_rank_sorted[0][0], count_to_rank_sorted[1][0], count_to_rank_sorted[1][1], count_to_rank_sorted[1][2]]]
    else:
        return [1, count_to_rank_sorted[0][:5]]

def determine_winner(player1_cards, player2_cards):
    rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    player1_combo = determine_combo(player1_cards)
    player2_combo = determine_combo(player2_cards)
    print(player1_combo)
    print(player2_combo)
    # print()

    if player1_combo[0] > player2_combo[0]:
        return 1
    elif player1_combo[0] < player2_combo[0]:
        return 2
    else:
        for l in range(len(player1_combo[1])):
            if rank.index(player1_combo[1][l]) != rank.index(player2_combo[1][l]):
                if rank.index(player1_combo[1][l]) < rank.index(player2_combo[1][l]):
                    return 1
                else:
                    return 2
        return 0
    '''
    else:
        rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        for l in range(len(player1_combo[1])):
            for r in rank:
                if not (r in player1_combo[1].keys() and r in player2_combo[1].keys()):#not in both
                    if r in player1_combo[1].keys():
                        return 1
                    elif r in player2_combo[1].keys():
                        return 0
    '''


print("A high flush over K high flush")
players = []
players.append([Card('A', 'H'),
                Card('2', 'D')])
players.append([Card('K', 'H'),
                Card('2', 'C')])
board = [Card('9', 'H'),
         Card('8', 'H'),
         Card('7', 'H'),
         Card('6', 'H'),
         Card('3', 'C')]
determine_winner(players[0] + board, players[1] + board)

print("K high flush over Q high flush")
players = []
players.append([Card('Q', 'H'),
                Card('2', 'D')])
players.append([Card('K', 'H'),
                Card('2', 'C')])
board = [Card('A', 'H'),
         Card('8', 'H'),
         Card('7', 'H'),
         Card('6', 'H'),
         Card('3', 'C')]
determine_winner(players[0] + board, players[1] + board)

print("One pair and 3 kickers")
players = []
players.append([Card('T', 'H'),
                Card('T', 'C')])
players.append([Card('2', 'H'),
                Card('2', 'C')])
board = [Card('3', 'D'),
         Card('K', 'H'),
         Card('J', 'C'),
         Card('4', 'D'),
         Card('Q', 'C')]
determine_winner(players[0] + board, players[1] + board)

print("High card")
players = []
players.append([Card('T', 'H'),
                Card('3', 'C')])
players.append([Card('3', 'H'),
                Card('5', 'C')])
board = [Card('Q', 'D'),
         Card('J', 'H'),
         Card('K', 'C'),
         Card('2', 'D'),
         Card('4', 'C')]
determine_winner(players[0] + board, players[1] + board)

print("Straight flush over straight flush")
players = []
players.append([Card('5', 'H'),
                Card('2', 'D')])
players.append([Card('T', 'H'),
                Card('2', 'C')])
board = [Card('9', 'H'),
         Card('8', 'H'),
         Card('7', 'H'),
         Card('6', 'H'),
         Card('3', 'C')]
determine_winner(players[0] + board, players[1] + board)

print("Royal flush")
players = []
players.append([Card('K', 'H'),
                Card('J', 'H')])
players.append([Card('3', 'H'),
                Card('2', 'C')])
board = [Card('A', 'H'),
         Card('Q', 'H'),
         Card('T', 'H'),
         Card('6', 'H'),
         Card('3', 'C')]
determine_winner(players[0] + board, players[1] + board)

print("Full house")
players = []
players.append([Card('T', 'H'),
                Card('T', 'D')])
players.append([Card('3', 'H'),
                Card('2', 'C')])
board = [Card('K', 'S'),
         Card('K', 'H'),
         Card('K', 'C'),
         Card('2', 'H'),
         Card('2', 'C')]
determine_winner(players[0] + board, players[1] + board)

print("Full house")
players = []
players.append([Card('A', 'H'),
                Card('A', 'D')])
players.append([Card('3', 'H'),
                Card('2', 'C')])
board = [Card('A', 'S'),
         Card('K', 'H'),
         Card('K', 'C'),
         Card('K', 'H'),
         Card('2', 'C')]
determine_winner(players[0] + board, players[1] + board)

print("Flush")
players = []
players.append([Card('A', 'D'),
                Card('2', 'D')])
players.append([Card('3', 'H'),
                Card('2', 'C')])
board = [Card('6', 'D'),
         Card('4', 'D'),
         Card('K', 'D'),
         Card('2', 'H'),
         Card('2', 'C')]
determine_winner(players[0] + board, players[1] + board)

print("Straight")
players = []
players.append([Card('A', 'D'),
                Card('6', 'D')])
players.append([Card('A', 'H'),
                Card('2', 'C')])
board = [Card('2', 'D'),
         Card('3', 'S'),
         Card('4', 'D'),
         Card('5', 'H'),
         Card('2', 'C')]
determine_winner(players[0] + board, players[1] + board)

player1_count = 0
for i in range(10):
    deck = shuffle()
    players = []
    number_of_players = 2
    for p in range(number_of_players):
        players.append(deck[:2])    #deal two cards
        deck = deck[2:]             #remove two cards
    printCards(players[0])
    printCards(players[1])
    family = deck[:5]
    printCards(family)
    players[0].extend(family)
    players[1].extend(family)
    result = determine_winner(players[0], players[1])
    print(str(result))
    print()
    player1_count += result
'''
PROBLEMPROBLEMPROBLEMPROBLEMPROBLEMPROBLEMPROBLEM
QD KH
8S JH
5H QH 6H 9H 7C
[6, ['K', 'Q', '9', '6', '5']]
[9, ['9', '8', '7', '6', '5']]
2
'''