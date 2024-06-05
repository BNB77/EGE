from functools import lru_cache


def pos(n):
    return n + 1, n * 2
@lru_cache(None)
def f(n):
    if any(x >= 181 for x in pos(n)):
        return 1
    if all(f(x) == 1 for x in pos(n)):
        return 2
    if any(f(x) == 2 for x in pos(n)):
        return 3
    if all(f(x) == 1 or f(x) == 3 for x in pos(n)):
        return 4
for s in range(1, 181):
    if f(s) == 4:
        print(s)
