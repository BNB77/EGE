data = {}
with open("26.txt", "r") as f:
    f.readline()
    for line in f.readlines():
        row, column = map(int, line.split())
        if data.get(row):
            data[row].add(column)
        else:
            data[row] = {column,}

maxrow = maxlen = 0
for row in sorted(data.keys(), reverse=True):
    line = sorted(data[row])
    currlen = 0
    maxline = 0
    for i in range(len(line)-1):
        if line[i+1] - line[i] - 1 <= 7:
            currlen += line[i+1] - line[i]
            maxline = max(maxline, currlen + 1)
        else:
            currlen = 0
    if maxline > maxlen:
        maxlen = maxline
        maxrow = row
print(maxlen, maxrow)