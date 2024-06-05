from functools import lru_cache


def pos(n):
    return n + 1, n + 3, n * 2
@lru_cache(None)
def f(n):
    if any(x >= 42 for x in pos(n)):
        return 1
    if any(f(x) == 1 for x in pos(n)):
        return 2
for s in range(1, 41):
    if f(s) == 2:
        print(s)
