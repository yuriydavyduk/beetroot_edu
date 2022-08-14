class WithIndexClass:
    def __init__(self, iterable, start: int = 0):
        self.iterable = iterable
        self.start = start - 1
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.iterable) - 1:
            raise StopIteration

        self.start += 1

        return self.start, self.iterable[self.index]


def with_index(iterable, start: int = 0):
    index = start
    for elem in iterable:
        yield index, elem
        index += 1


r = [1, 2, 3, 4, 5]
# wic = with_index(r, 10)
wic = WithIndexClass(r, 0)

for i, j in wic:
    print(i, j)
