__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem Statement:
Bingo 5x5 square 1-75 numbers
'''
import random

used = []
def randNum():
    rand_number = random.randrange(75)+1
    while rand_number in used:
        rand_number = random.randrange(75)+1
    used.append(rand_number)
    return rand_number

db =
board = [[randNum() for x in range(5)] for y in range(5)]
for x in range(5):
    print(board[x])
    for y in range(5):
        print(board[y][x], end=" ")