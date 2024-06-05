f = open('26 (1).txt')n = int(f.readline())
start = 1634515199
end = start + 604800
count = 0
time = [0 for i in range(604801)]
for i in f:    start1, end1 = i.split()
    if (int(start1) < start) and ((int(end1) > start) or (int(end1) == 0)):
        count = count + 1
    if (int(start1) >= start) and (int(start1) <= end):
        time[int(start1) - start] = time[int(start1) - start] + 1
    if (int(end1) >= start) and (int(end1) <= end):
        time[int(end1) - start] = time[int(end1) - start] - 1
s = 0
m = 0
for i in range(1, 604801):    count = count + time[i]
    if count > m:
        m = count
        s = 0
        if count == m:
            s = s + 1
            print(m, s)