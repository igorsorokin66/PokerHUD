__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''


rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
suit = ["S", "H", "C", "D"]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

def shuffle():
    import random
    deck = ["" for i in range(1, 53)]
    avail = [i for i in range(0, 52)]
    for r in rank:
        for s in suit:
            randNum = random.sample(avail, 1)
            avail.remove(randNum[0])
            deck[randNum[0]] = r + s
    return deck

def order_by_rank(cards):
    rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    cards_dict_by_rank_index = {card: rank.index(card) for card in cards}
    cards_sorted_by_rank_index = sorted(cards_dict_by_rank_index, key=cards_dict_by_rank_index.get)
    return cards_sorted_by_rank_index

def determine_combo(cards):
    suit = ["C", "S", "H", "D"]
    suit_count = dict(zip(suit, [[] for i in range(0, 4)]))
    rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    rank_count = dict(zip(rank, [0 for i in range(0, 13)]))
    flush_flag = False
    for card in cards:
        suit_count[card.suit].append(card)
        rank_count[card.rank] += 1
        if len(suit_count[card.suit]) == 5:
            flush_flag = True
            flush_suit = card.suit

    cards_no_duplicates = {key: rank_count[key] for key in rank_count if rank_count[key] != 0}
    cards_ordered_by_rank = order_by_rank(cards_no_duplicates.keys())
    Ato5 = [rank[0]] + rank[9:13]#Exception A,2,3,4,5
    for i in range(0, 9):
        if cards_ordered_by_rank[:5] == rank[0+i:5+i] or cards_ordered_by_rank[:5] == Ato5:
            if flush_flag:
                if i is 0:
                    return 10#Royal Flush
                else:
                    return [9, cards_ordered_by_rank[:5]]#Straight Flush
            else:
                return [5, cards_ordered_by_rank[:5]]#Straight

    if flush_flag:
        flush_cards = [card.rank for card in suit_count[flush_suit]]
        flush_cards_ordered_by_rank = order_by_rank(flush_cards)
        return [6, flush_cards_ordered_by_rank]#Flush

    if rank_count[rank_count_sorted[0]] == 4:
        return [8, rank_count]#Four of a Kind
    elif rank_count[rank_count_sorted[0]] == 3 and rank_count[rank_count_sorted[1]] == 2:
        return [7, rank_count]#Full House
    elif rank_count[rank_count_sorted[0]] == 3:
        return [4, rank_count]#Three of a Kind
    elif rank_count[rank_count_sorted[0]] == 2 and rank_count[rank_count_sorted[1]] == 2:
        return [3, rank_count]#Two Pair
    elif rank_count[rank_count_sorted[0]] == 2:
        return [2, rank_count_sorted]#One Pair
    else:
        return [1, rank_count_sorted]

def determine_winner(player1_cards, player2_cards):
    rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    player1_combo = determine_combo(player1_cards)
    player2_combo = determine_combo(player2_cards)
    if player1_combo[0] > player2_combo[0]:
        return 1
    elif player1_combo[0] < player2_combo[0]:
        return 2
    elif player1_combo[0] == 1:#compare high cards
        for r in rank:
            for l in range(len(player1_combo[1])):
                if not (r is player1_combo[1][l] and r is player2_combo[1][l]):#not in both
                    if r is player1_combo[1][l]:
                        return 1
                    elif r is player2_combo[1][l]:
                        return 0
    elif player1_combo[0] == 2:#compare one pair
        misc = 0
    elif player1_combo[0] == 3:#compare two pair
        misc = 0
    elif player1_combo[0] == 4:#compare three of a kind
        misc = 0
    elif player1_combo[0] == 5:#compare straight
        misc = 0
    elif player1_combo[0] == 6:#compare flush
        for i in range(len(player1_combo[1])):
            player1_flush_card_rank = player1_combo[1][i]
            player2_flush_card_rank = player2_combo[1][i]
            if player1_flush_card_rank != player2_flush_card_rank:
                if rank.index(player1_flush_card_rank) < rank.index(player2_flush_card_rank):
                    return 1
                else:
                    return 2
        return 0#chopped flush
    elif player1_combo[0] == 7:#compare full house
        misc = 0
    elif player1_combo[0] == 8:#compare quads
        misc = 0
    elif player1_combo[0] == 9:#compare straight flushs
        misc = 0
    else:#chop chop
        misc = 0
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
'''
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
print("Resulted: Player " + str(determine_winner(players[0] + board, players[1] + board)))
print("Expected: Player 1")

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
print("Resulted: Player " + str(determine_winner(players[0] + board, players[1] + board)))
print("Expected: Player 2")
'''
players = []
players.append([Card('T', 'H'),
                Card('4', 'C')])
players.append([Card('2', 'H'),
                Card('2', 'C')])
board = [Card('9', 'H'),
         Card('K', 'H'),
         Card('Q', 'H'),
         Card('J', 'H'),
         Card('3', 'C')]
print("Resulted: Player " + str(determine_winner(players[0] + board, players[1] + board)))
print("Expected: Player 2")

'''
player1_count = 0
for i in range(10000):
    deck = shuffle()
    players = []
    number_of_players = 2
    for p in range(number_of_players):
        players.append(deck[:2])    #deal two cards
        deck = deck[2:]             #remove two cards
    print(players)
    family = deck[:5]
    players[0].extend(family)
    players[1].extend(family)
    print(str(determine_winner(players[0], players[1])))
    player1_count += determine_winner(players[0], players[1])
'''