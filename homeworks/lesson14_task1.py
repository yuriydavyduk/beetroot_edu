def logger(func):
    def wrap(*args):
        print(func.__name__, args, sep='')
        return func(*args)

    return wrap


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


print(add(4, 5))
print(square_all(4, 5))
