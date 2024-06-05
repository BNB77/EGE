
from math import ceil
f = open('27_B.txt')
n = int(f.readline())
elems = []
leftsumm = 0
rightsumm = 0
cost = [0] * n
for i in range(0, n):
    a, b = map(int, f.readline().split())
    elems.append([a, ceil(b / 36)])
for i in elems[1:]:
    cost[0] += (i[0] - elems[0][0]) * i[1]
    rightsumm += i[-1]
smin = rightsumm + 0
for i in range(1, n):
    x = elems[i]
    r, n = x
    leftsumm += elems[i- 1][1]
    cost[i] = cost[i - 1] - rightsumm * (r - elems[i - 1][0]) + leftsumm * (r - elems[i - 1][0])
    rightsumm -= elems[i][1]

print(min(cost))