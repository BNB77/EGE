f = open('28130_A.txt')
n = int(f.readline())
m = 80
data = [int(x) for x in f]
ost50 = [0 for x in range(m)]
ost = [0 for x in range(m)]
ans = 0
for x in data:
    if x > 50:
        ost50[x % m] += 1
    else:
        ost[x % m] += 1
for p in range(1, 40):
    ans += ((ost[p]+ost50[p]) * ost50[m - p] + ost50[p] * ost[m - p])
ans += ost50[0] * (ost50[0] - 1) // 2 + ost50[0] * ost[0]
ans += ost50[40] * (ost50[40] - 1) // 2 + ost50[40] * ost[40]
print(ans)
