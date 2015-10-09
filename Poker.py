#Time: 1 hour, 30 minutes
import random

rank = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
suit = ["Spades", "Hearts", "Clubs", "Diamonds"]

def shuffle():
    deck = ["" for i in range(1,53)]
    avail = [i for i in range(0,52)]
    for r in rank:
        for s in suit:
            randNum = random.sample(avail,1)
            avail.remove(randNum[0])
            deck[randNum[0]] = r + " of " + s
    #print(deck[:5])
    return deck

def identify(cards):
    flush = dict(zip(suit,[0 for i in range(0,4)]))#spades 0 hearts 0 clubs 0 diam 0
    rankD = {}
    for c in cards:
        r = c.split(" of ")[0]
        s = c.split(" of ")[1]
        flush[s] = flush[s]+1
        if r in rankD.keys():
            rankD[r] = rankD[r]+1
        else:
            rankD[r] = 1
        
    #print(flush)
    flushS = sorted(flush, key=flush.get)
    flushS.reverse()
    #print(flushS)

    #print(rankD)
    rankS = sorted(rankD)
    rankS.reverse()
    #print(rankS)

    Ato5 = [rank[0]]#Exception A,2,3,4,5
    Ato5.extend(rank[9:13])
    for i in range(0,9):
        #print(rank[0+i:5+i])
        if rankS == rank[0+i:5+i] or rankS == Ato5:
            if flush[flushS[0]] is 5:
                if i is 0:
                    #print("Royal Flush")
                    return 0
                else:
                    #print("Straight Flush")
                    return 1
            else:
                #print("Straight")
                return 5
    if flush[flushS[0]] is 5:
        #print("Flush")
        return 4
    if len(rankS) is 2:
        if rankD[rankS[0]] is 4:
            #print("Four of a Kind")
            return 2
        else:
            #print("Full House")
            return 3
    if len(rankS) is 3:
        if rankD[rankS[0]] is 3:
            #print("Three of a Kind")
            return 6
        else:
            #print("Two Pair")
            return 7
    if len(rankS) is 4:
        #print("One Pair")
        return 8
    return 9

def getStats():
    stats = [0,0,0,0,0,0,0,0,0,0]
    for i in range(0,10000):
        deck = shuffle()
        num = identify(deck[:5])
        stats[num] = stats[num]+1
    print("Royal Flush "+str(stats[0]))
    print("Straight Flush "+str(stats[1]))
    print("Four of a Kind "+str(stats[2]))
    print("Full House "+str(stats[3]))
    print("Flush "+str(stats[4]))
    print("Straight "+str(stats[5]))
    print("Three of Kind "+str(stats[6]))
    print("Two Pair "+str(stats[7]))
    print("One Pair "+str(stats[8]))
    print("Nothing "+str(stats[9]))

getStats()