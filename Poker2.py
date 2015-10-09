__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''


rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
suit = ["S", "H", "C", "D"]

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

def determine_combo(cards):
    suit = ["C", "S", "H", "D"]
    suit_count = dict(zip(suit, [0 for i in range(0, 4)]))
    #{'H': 0, 'D': 0, 'C': 0, 'S': 0}
    rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    rank_count = dict(zip(rank, [0 for i in range(0, 13)]))
    for card in cards:
        suit_count[card[1]] += 1
        rank_count[card[0]] += 1

    suit_count_sorted = sorted(suit_count, key=suit_count.get)
    suit_count_sorted.reverse()
    #['S', 'C', 'H', 'D']
    flush_flag = False
    if suit_count[suit_count_sorted[0]] == 5:
        flush_flag = True

    rank_count = {key: rank_count[key] for key in rank_count if rank_count[key] != 0}
    rank_count_sorted = sorted(rank_count, key=rank_count.get)
    rank_count_sorted.reverse()

    Ato5 = [rank[0]]#Exception A,2,3,4,5
    Ato5.extend(rank[9:13])
    for i in range(0, 9):
        if sorted(rank_count_sorted[:5]) == sorted(rank[0+i:5+i]) or sorted(rank_count_sorted[:5]) == sorted(Ato5):
            if flush_flag:
                if i is 0:
                    return 0#Royal Flush
                else:
                    return [1, rank_count]#Straight Flush
            else:
                return [5, rank_count]#Straight

    if flush_flag:
        return [6, rank_count]#Flush

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
    player1_combo = determine_combo(player1_cards)
    player2_combo = determine_combo(player2_cards)
    if player1_combo[0] > player2_combo[0]:
        return 1
    elif player1_combo[0] < player2_combo[0]:
        return 0
    elif player1_combo[0] == 1:
        rank = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        for r in rank:
            for l in range(len(player1_combo[1])):
                if not (r is player1_combo[1][l] and r is player2_combo[1][l]):#not in both
                    if r is player1_combo[1][l]:
                        return 1
                    elif r is player2_combo[1][l]:
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

player1_count = 0
for i in range(10000):
    deck = shuffle()
    players = []
    number_of_players = 2
    for p in range(number_of_players):
        players.append(deck[:2])    #deal two cards
        deck = deck[2:]             #remove two cards
    print players
    family = deck[:5]
    players[0].extend(family)
    players[1].extend(family)
    print(str(determine_winner(players[0], players[1])))
    player1_count += determine_winner(players[0], players[1])