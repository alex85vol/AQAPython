import functools


def sum_for(iter):
    res = 0
    for i in iter:
        res += i
    return res


def sum_reduce(iter):
    return functools.reduce(lambda a, b: a + b, iter)


if __name__ == "__main__":
    print('Using for: ' + str(sum_for(range(20))))
    print('Using reduce: ' + str(sum_reduce(range(20))))
