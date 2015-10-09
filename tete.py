__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = ''

import math
t = "6 3"#input().strip()
x, y = t.split(" ")
#x = int(t.split(" ")[0])
#y = int(t.split(" ")[1])
tot = (math.ceil(x/float(2))-1)*10
'''
if x % 2 == 0:
    tot += y*2-1
else:
    tot += y*2-2
print(tot)
'''
print(tot+y*2-1 if x % 2==0 else tot+y*2-2)

