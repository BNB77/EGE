f = open('107_27_A.txt')
n = int(f.readline())
data = [int(x) for x in f]
S = 0
Smin = 100 ** 100
for i in range(n // 2 + 1):
    S += data[i] * i * 3
for i in range(n // 2 + 1, n):
    S += data[i] * (n - i) * 3
l = data[0]
i1 = n // 2 + 1
for i in range(n // 2 + 1, n):
    l += data[i]

r = 0
i2 = 1
for i in range(1, n // 2 + 1):
    r += data[i]

for i in range(n):
    S += (l - r) * 3
    l += (data[i2] - data[i1])
    r += (data[i1] - data[i2])
    i1 = (i1 + 1) % n
    i2 = (i2 + 1) % n
    Smin = min(S, Smin)

print(Smin)
