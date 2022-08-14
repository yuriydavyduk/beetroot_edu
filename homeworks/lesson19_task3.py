class InPower:
    def __init__(self, _start: int, _stop: int = None, step: int = 1, power: int = 1):
        if step == 0:
            raise ValueError('arg 3 must not be zero')

        self.start = _start if _stop is not None else 0
        self.stop = _stop if _stop is not None else _start
        self.step = step
        self.power = power
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):

        self.index += 1

        res = self.start + self.step * self.index

        if self.step > 0 and res >= self.stop:
            raise StopIteration

        if self.step < 0 and res <= self.stop:
            raise StopIteration

        return res ** self.power

    def __getitem__(self, item):

        res = self.start + self.step * item
        if self.step > 0 and res >= self.stop:
            raise IndexError('range object index out of range')

        if self.step < 0 and res <= self.stop:
            raise IndexError('range object index out of range')

        return res ** self.power


result = InPower(0, 10, 1, 2)

for i in result:
    print(i)

assert result[6] == 6**2
