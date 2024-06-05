import math


f = open('27_B.txt')
N, M = [int(i.strip()) for i in f.readline().split()]
A = [[int(i.split()[0]), math.ceil(int(i.split()[1]) / 15)] for i in f.readlines()]
j = 0
h = 0
ans = 0
k = 0
for x in range(N):
    while h < N and A[h][0] - A[x][0] <= M:
        k += A[h][1]
        h += 1
    while int(A[x][0]) - M > int(A[j][0]):
        k -= A[j][1]
        j += 1
        ans = max(ans, k)
print(ans)
