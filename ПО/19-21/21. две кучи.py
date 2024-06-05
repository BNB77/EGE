from functools import lru_cache


def pos(n, k):
    return (n + 1, k), (n * 4, k), (n, k + 1), (n, k * 4)


@lru_cache(None)
def f(n, k):
    if any(x + y >= 82 for x, y in pos(n, k)):
        return 1
    if all(f(x, y) == 1 for x, y in pos(n, k)):
        return 2
    if any(f(x, y) == 2 for x, y in pos(n, k)):
        return 3
    if all(f(x, y) == 1 or f(x, y) == 3 for x, y in pos(n, k)):
        return 4
for s in range(1, 77):
    if f(4, s) == 4:
        print(s)
