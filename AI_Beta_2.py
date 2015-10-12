__author__ = 'isoroki'
import random

class Player:
    def __init__(self, name):
        self._name = name
        self._chips = 200
        self._infor = 0
        self._inhand = False
    def setPosition(self, position):
        self._position = position
    def winChips(self, profit):
        self._chips += profit
    def loseChips(self, losses):
        self._chips -= losses
    def bets(self, bet):
        self._infor += bet
        self._chips -= bet
    def inFor(self):
        return self._infor

def analyze(player):
    bigBlind = 5
    smallBlind = 2
    if player._position == "BUT":
        player.bets(15)
        print(player._name  +"\t("+player._position+")\t"+    " bets "        + str(15))
        return 15
    elif player._position == "BB":
        player.bets(bigBlind)
        print(player._name  +"\t("+player._position+")\t"+    " pays BB of "  + str(bigBlind))
        return 5
    elif player._position == "SB":
        player.bets(smallBlind)
        print(player._name  +"\t("+player._position+")\t"+    " pays SB of "  + str(smallBlind))
        return 2
    else:
        print(player._name  +"\t("+player._position+")\t"+    " folds")
        return 0

playerIgor = Player("Igor")
playerJohn = Player("John")
playerLee = Player("Leee")
playerPaul = Player("Paul")
playerArian = Player("Arian")
playerYianni = Player("Yianni")

playerList = [playerArian, playerIgor, playerJohn, playerLee, playerPaul, playerYianni]
random.shuffle(playerList)
print([player._name for player in playerList])


positions = ["UTG", "EARL", "LATE", "BUT", "SB", "BB"]
positionToPlayer = {}
for player, position in zip(playerList, positions):
    player.setPosition(position)
    positionToPlayer[position] = player
print([player._position for player in playerList])

#postflop
actionIsOngoing = True
pot = 0
currentBet = 5
while actionIsOngoing:
    for position in positions:
        currentPlayer = positionToPlayer[position]
        if currentBet == currentPlayer.inFor():
            actionIsOngoing = False
            break
        bet = 0
        player._inhand = True
        if player._inhand:
            bet = analyze(currentPlayer)
        pot += bet
        if bet >= currentBet:
            currentBet = bet
            player._inhand = True

print("------------------------")

postFlopPositions = ["SB", "BB", "UTG", "EARL", "LATE", "BUT"]
currentBet = 0
actionIsOngoing = True
while actionIsOngoing:
    for position in postFlopPositions:
        currentPlayer = positionToPlayer[position]
        if currentBet == currentPlayer.inFor():
            actionIsOngoing = False
            break
        bet = 0
        player._inhand = True
        if player._inhand:
            bet = analyze(currentPlayer)
        pot += bet
        if bet >= currentBet:
            currentBet = bet
            player._inhand = True

