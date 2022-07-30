class FirstClass:
    class_atr = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def do_something(self, temp):
        print(f'A: {self.a}. B: {self.b}')
        return self.a + self.b, FirstClass(self.a + self.b, self.a + self.b)

x = FirstClass(1,2)
y = FirstClass(3,4)

z = x.do_something(y)

print(z[1].b)