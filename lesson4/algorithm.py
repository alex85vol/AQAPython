def algorythm_01():
    s = list(filter(lambda a: a % 3 == 0, range(100)))
    return print(s)


if __name__ == "__main__":
    print(algorythm_01())
