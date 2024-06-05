from itertools import product
c = 0
for i, v in enumerate(product(sorted("АЛГОРИТМ"), repeat=5), start=1):
    if i % 2 != 0 and v[0] != "Г" and v.count("И") >= 2:
        c += 1
print(c)