class Complex(object):

    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y

    def __str__(self):
        z = '+'
        if self.y < 0:
            z = ''
        return format(self.x, '.2f') + z + format(self.y, '.2f') + 'i'

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, other.x * self.y + self.x * other.y)

    def __truediv__(self, other):
        r_n = other.x ** 2 + other.y ** 2
        r1 = self.x * other.x + self.y * other.y
        r2 = self.y * other.x - self.x * other.y
        return Complex(r1/r_n, r2/r_n)

    def __abs__(self):
        return Complex((self.x ** 2 + self.y ** 2) ** 0.5, 0)


def main(s1, s2):
    c = Complex(int(s1.split()[0]), int(s1.split()[1]))
    d = Complex(int(s2.split()[0]), int(s2.split()[1]))
    print(c + d)
    print(c - d)
    print(c * d)
    print(c / d)
    print(abs(c))
    print(abs(d))


ss1 = '2 1'
ss2 = '5 6'
main(ss1, ss2)
