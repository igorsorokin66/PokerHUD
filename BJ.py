__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''

rank = ["11", "10", "10", "10", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
suit = ["C", "S", "H", "D"]

def generate_deck():
    import random
    deck = ["" for i in range(1, 53)]
    avail = [i for i in range(0, 52)]
    for r in rank:
        for s in suit:
            randNum = random.sample(avail, 1)
            avail.remove(randNum[0])
            deck[randNum[0]] = r
    return deck

shoe = generate_deck()
shoe.extend(generate_deck())
shoe.extend(generate_deck())
shoe.extend(generate_deck())
shoe.extend(generate_deck())
shoe.extend(generate_deck())

stack = 500
for i in range(0, len(shoe), 4):
    deal = [shoe[i], shoe[i+1]]
    you = [shoe[i+2], shoe[i+3]]

    if sum(you) == 21:#blackjack
        if sum(deal) != 21:
            stack += 3
    else:
        if sum(you) >= deal[0] + 10:
            deal.append(shoe[i])