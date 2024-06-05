f = open('24 (1).txt')
v = f.readline()
kmx = 0
k = 0
c = 0
j = 0
for i in range(len(v)):
    if v[i] == 'A':
        k += 1
        c += 1
    if k > 35:
        while k > 35:
            if v[j] == 'A':
                k -= 1
                if k == 35:
                    kmx = max(kmx, i - j + 1)
            j += 1
            print(kmx)