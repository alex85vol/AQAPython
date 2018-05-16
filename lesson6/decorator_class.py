import functools


class dec(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self.func(*args) * functools.reduce(lambda a, b: a + b, args)


@dec
def s(a, b):
    return b % a


if __name__ == '__main__':
    print(s(6, 8))
    f = dec(lambda a, b: a + b)
    print(f(4, 5))
    print(dec(lambda a, b, c: a * b / c)(54, 87, 66))
