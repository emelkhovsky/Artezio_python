def cycle(n):
    while True:
        for i in n:
            yield i


def main():
    a = cycle([1, 2, 3])
    return a


rezult = main()
print(next(rezult))  # 1
print(next(rezult))  # 2
print(next(rezult))  # 3
print(next(rezult))  # 1
print(next(rezult))  # 2
print(next(rezult))  # 3
