f = open('24.txt').readline().replace('C', 'C ').replace('D', "D ").split()
m = 0
for i in range(len(f) - 4):
    r = f[i] + f[i + 1] + f[i + 2] + f[i + 3] + f[i + 4][:-1]
    if r.count('C') == 2 and r.count('D') == 2:
        m = max(m, len(r))
print(m)