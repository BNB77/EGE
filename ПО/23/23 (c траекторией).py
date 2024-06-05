def func(number, end):
    if number < end:
        return 0
    if number == end:
        return 1
    return func(number - 1, end) + func(number // 2, end)


print(func(60, 10) * func(10, 2))
