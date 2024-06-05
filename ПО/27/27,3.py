f = open('27-B.txt')
n = int(f.readline())
data = [x for x in f]
s1 = 0
s2 = 0
s3 = 0
dmin = 10 ** 10
for x in data:
    a, b, c = [int(i) for i in x.split()]
    d1 = max(a, b, c)
    d2 = (a + b + c) - max(a, b, c) - min(a, b, c)
    d3 = min(a, b, c)
    if (d2 - d3) % 2 == 1:
        dmin = min(dmin, d2 - d3)
    if (d1 - d3) % 2 == 1:
        dmin = min(dmin, d1 - d3)
    s1 += d1
    s2 += d2
    s3 += d3
print(s1)
print(s2)
print(s3 + dmin)