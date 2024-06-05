f = open('26 (1).txt')b = []
c =[]
for i in f:
    s, col = i.split()
    b.append([int(s), col])
b.sort(reverse=True)
while len(b) > 0:
    block = [b.pop(0)]
    for j in range (len(b)):
        if block[-1][0] - b[j][0] >= 7 and b[j][1] != block[-1][1]:
            block.append(b[j])
            b[j] = ''
            b = [x for x in b if x != '']
    c.append(block)
    print(max(len(x) for x in c), len(c))