f = open('27_B.txt')
n = int(f.readline())
data = [int(x) for x in f]
k = 89
smax = 0
lmin = 10  20
m = [10  20] * k
l = [0] * k
s = 0
for i in range(n):
    x = data[i]
    s += x
    if s % k == 0:
        if s > smax or (s == smax and i + 1 < lmin):
            smax = max(smax, s)
            lmin = i + 1

    s1 = s - m[s % k]
    l1 = i + 1 - l[s % k]
    if s1 > smax or (s1 == smax and l1 < lmin):
        smax = max(smax, s)
        lmin = l1

    if s < m[s % k]:
        m[s % k] = s
        l[s % k] = i + 1
print(smax, lmin)