from functools import lru_cache
def pos(n, k):
    return (n + 1, k), (n * 4, k), (n, k + 1), (n, k * 4)
@lru_cache(None)
def f(n, k):
    if any(x + y >= 82 for x, y in pos(n, k)):
        return 1
    if any(f(x, y) == 1 for x, y in pos(n, k)):
        return 2
for s in range(1, 77):
    if f(4, s) == 2:
        print(s)
