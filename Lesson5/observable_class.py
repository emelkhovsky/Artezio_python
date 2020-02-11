class Observable(object):

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        s = ''
        for i in dir(self):
            if not i.startswith('_'):
                s += i + '=' + str(getattr(self, i)) + ', '
        return s


class X(Observable):
    pass


def main():
    x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
    print(x.props)  # ('One', 'two')
    print(x.bar)  # 5
    print(x._bazz)  # 12
    print(x)


main()

