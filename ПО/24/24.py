f = open("24.txt")
s = f.readline()
f.close()
#s = "FFFSWYFFSWYFSWYFFSWYFYYY"
print(len(s))
print(s[:40])
a = "FSWYFSWY"
maxlen = 0
p0 = 0
while p0 < len(s):
    if s[p0:p0 + 2] in a:
        p1 = p0 + 1
        while p1 < len(s) and s[p1:p1 + 2] in a:
            p1 += 1
        if len(s[p0:p1 + 1]) > maxlen:
            maxlen = len(s[p0:p1 + 1])
            print(maxlen, s[p0:p1 + 1])
        p0 = p1
    p0 += 1