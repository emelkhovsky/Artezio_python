class EvenIterator(object):

    def __init__(self, limit):
        self.limit = limit
        self.current = -2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit - 2:
            self.current += 2
            return self.current
        else:
            raise StopIteration


def main(ma):
    n_ma = []
    for i in EvenIterator(len(ma)):
        n_ma.append(m[i])
    return n_ma


m = ['a', 'b', 'c', 'd', 'e']
rezult = main(m)
print(rezult)
