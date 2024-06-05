timeline = [None] * 60 * 24
with open("26-2.txt", "r") as f:
    r = f.readline()
    for line in f.readlines():
        arrival, duration, windownum = map(int, line.split())
        timeline[arrival - 1] = [duration, windownum]
o1 = []
o2 = []
l1 = 0
l2 = 0

k1 = 0
left = 0
for minute in timeline:
    if l1 > 0:
        o1[0] -= 1
        if o1[0] == 0:
            o1.pop(0)
            k1 += 1
            l1 -= 1
    if l2 > 0:
        o2[0] -= 1
        if o2[0] == 0:
            o2.pop(0)
            l2 -= 1
    if l1 == 12 and l2 == 12:
        left += 1
    else:
        if minute is not None:
            if minute[1] == 1:
                if l1 == 12:
                    left += 1
                elif l1 < 12:
                    o1.append(minute[0])
                    l1 += 1
            elif minute[1] == 2:
                if l2 == 12:
                    left += 1
                elif l2 < 12:
                    o2.append(minute[0])
                    l2 += 1
            else:
                if l1 < 12:
                    o1.append(minute[0])
                    l1 += 1
                elif l2 < 12:
                    o2.append(minute[0])
                    l2 += 1
print(k1, left)