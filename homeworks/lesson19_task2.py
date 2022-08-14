class InRange:
    def __init__(self, _start: int, _stop: int = None, step: int = 1):
        if step == 0:
            raise ValueError('arg 3 must not be zero')

        self.start = _start if _stop is not None else 0
        self.stop = _stop if _stop is not None else _start
        self.step = step
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

        return res

    def __getitem__(self, item):

        res = self.start + self.step * item
        if self.step > 0 and res >= self.stop:
            raise IndexError('range object index out of range')

        if self.step < 0 and res <= self.stop:
            raise IndexError('range object index out of range')

        return res


def in_range(_start: int, _stop: int = None, step: int = 1):
    if step == 0:
        raise ValueError('arg 3 must not be zero')

    start = _start if _stop is not None else 0
    stop = _stop if _stop is not None else _start
    i = 0
    res = start

    while step > 0 and 0 <= i and res < stop:
        yield res
        i += 1
        res = start + step * i

    while step < 0 and 0 <= i and res > stop:
        yield res
        i += 1
        res = start + step * i


# With in_range
assert list(in_range(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert list(in_range(1, 11)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert list(in_range(0, 30, 5)) == [0, 5, 10, 15, 20, 25]

assert list(in_range(0, 10, 3)) == [0, 3, 6, 9]

assert list(in_range(0, -10, -1)) == [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

assert list(in_range(0)) == []

assert list(in_range(1, 0)) == []

# With class InRange
assert list(InRange(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

assert list(InRange(1, 11)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

assert list(InRange(0, 30, 5)) == [0, 5, 10, 15, 20, 25]

assert list(InRange(0, 10, 3)) == [0, 3, 6, 9]

assert list(InRange(0, -10, -1)) == [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]

assert list(InRange(0)) == []

assert list(InRange(1, 0)) == []
