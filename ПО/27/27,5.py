f = open('27-B.txt')
n = int(f.readline())
data = [int(x) for x in f]
k = 0
s = 0
l = [0] * 999
for i in range(n):
    x = data[i]
    s += x
    if s % 999 == 0:
        k += 1

    k += l[s % 999]
    l[s % 999] += 1
print(k)