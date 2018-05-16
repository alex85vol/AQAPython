def using_for():
    s = list()
    m = lambda x: x % 3 if x % 2 == 0 else 0

    for i in range(10):
        s.append(m(i))
    return s


def using_map():
    s = list(map(lambda x: x % 3 if x % 2 == 0 else 0, range(10)))
    return s


if __name__ == "__main__":

    print('Using for: ' + str(using_for()))
    print('Using map: ' + str(using_map()))
