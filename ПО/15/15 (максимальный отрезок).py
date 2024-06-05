m = 0
P = [i for i in range(5, 31)]
Q = [i for i in range(14, 24)]
for Amin in range(1, 101):
    for Amax in range(Amin + 1, 101):
        check = 1
        A = [i for i in range(Amin, Amax)]
        for x in range(1, 101):
            f = ((x in P) == (x in Q)) <= (not(x in A))
            if not f:
                check = 0
                break
        if check == 1:
            m = max(m, Amax - Amin)
print(m)