def nsd(a, b):
    while a*b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ZeroDivisionError
        _nsd = nsd(a, b)
        self.a = int(a/_nsd)
        self.b = int(b/_nsd)

    def __str__(self):
        return f'{self.a}/{self.b}'

    def __add__(self, other):
        return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)

    def __sub__(self, other):
        return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        return Fraction(self.a * other.b, self.b * other.a)

    def __eq__(self, other):
        return self.a/self.b == other.a/other.b

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    print(x + y == Fraction(3, 4))
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)