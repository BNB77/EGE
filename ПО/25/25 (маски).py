for i in range(307500,100000000,123):
    if str(i)[0:2] == '32' and str(i)[-3:] == '823':
        print(i, i // 123)
