__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''

rank = ["J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
suit = ["C", "S", "H", "D"]

def generate_deck():
    deck = []
    for r in rank:
        for s in suit:
            deck.append(r + s)
    return deck

deck = generate_deck()
count = 0
match = ['A', 'K', 'Q']
import itertools
for a, b, c, d, e in itertools.combinations(deck, 5):
    bin = []
    bin += [a[0],b[0],c[0],d[0],e[0]]
    deck1 = list(deck)
    if not any(bin.count(x) > 3 for x in bin) and not (a[0] in match or b[0] in match or c[0] in match or d[0] in match or e[0] in match):
        deck1.remove(a)
        deck1.remove(b)
        deck1.remove(c)
        deck1.remove(d)
        deck1.remove(e)
        #print(a + " "  + b + " "  + c + " "  + d + " "  + e + " " )
        for f, g, h in itertools.combinations(deck1, 3):#5
            bin1 = list(bin)
            bin1 += [f[0], g[0], h[0]]
            deck2 = list(deck1)
            if not any(bin1.count(x) > 3 for x in bin1) and not ((f[0] in match and g[0] in match) or (f[0] in match and h[0] in match) or (g[0] in match and h[0] in match)):
                deck2.remove(f)
                deck2.remove(g)
                deck2.remove(h)
                #print(f + " "  + g + " "  + h)
                for i, j, k in itertools.combinations(deck2, 3):#7
                    bin2 = list(bin1)
                    bin2 += [i[0], j[0], k[0]]
                    deck3 = list(deck2)
                    if not any(bin2.count(x) > 3 for x in bin2) and not ((i[0] in match and j[0] in match) or (i[0] in match and k[0] in match) or (j[0] in match and k[0] in match)):
                        deck3.remove(i)
                        deck3.remove(j)
                        deck3.remove(k)
                        #print(i + " "  + j + " "  + k)
                        for l, m, n in itertools.combinations(deck3, 3):#9
                            bin3 = list(bin2)
                            bin3 += [l[0], m[0], n[0]]
                            deck4 = list(deck3)
                            if not any(bin3.count(x) > 3 for x in bin3) and not ((l[0] in match and m[0] in match) or (l[0] in match and n[0] in match) or (m[0] in match and n[0] in match)):
                                #print(l + " "  + m + " "  + n)
                                deck4.remove(l)
                                deck4.remove(m)
                                deck4.remove(n)
                                for o, p, q in itertools.combinations(deck4, 3):#11
                                    if not ((o[0] in match and p[0] in match) or (o[0] in match and q[0] in match) or (p[0] in match and q[0] in match)):
                                        count += 1
                                        print(count)
                                        #print(a + " "  + b + " "  + c + " "  + d + " "  + e + " " + f + " " + g +" "+ h + " "+ i +" "+ j +" "+ k +" "+ l +" "+ m +" "+ n +" "+ o +" "+ p +" "+ q)
                                        #deck.remove(o)
                                        #deck.remove(p)
                                        #deck.remove(q)
                            deck4 = deck3
                    deck3 = deck2
            deck2 = deck1
        deck1 = deck

print(count)
