def chain(*args):
    for i in args:
        yield i


a = 'asd'
b = 123
c = [1,2,3]
d = {'cat': 1, 'dog': 2}
rezult = chain(a, b, c, d)
print(rezult)
print(next(rezult))
print(next(rezult))
print(next(rezult))
print(next(rezult))
