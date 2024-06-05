def f(x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)
    if max(x,y,z) < x + y + z - max(z,x,y):
        return 1
    return 0


r = set()
for A in range(100):
    g = True
    for x in range(100):
        if (not((f(x, 11, 16) == (not(max(x, 5) > 10))) and f(4, A, x))) == 0:
            g = False
            break
    if g:
        r.add(A)
print(max(r))