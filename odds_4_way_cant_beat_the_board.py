import random
import itertools
rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
suit = ["H", "D", "S", "C"]

pair = 0
nonpair = 0
misc = 0
bad = ["A", "K", "Q", 3, 8]
for i in itertools.combinations_with_replacement(rank, 2):
    if i[0] == i[1]:
        pair += 1
    else:
        nonpair += 1
        if i[0] not in bad and i[1] not in bad:
            print(i)
            misc += 1

total = pair * 6 + nonpair * 16
print(total)

misses = misc * 16
print(misses)#misses

print((misses/total) * (misses/total) * (misses/total) * (misses/total))

#all possible boards 52*51*50*49*48 311875200