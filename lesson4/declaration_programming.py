def functional(a):
    s = None
    if a > 10:
        s = 1
    else:
        s = 0
    return s


def declarative(a):
    s = 1 if a > 10 else 0
    return s


if __name__ == "__main__":
    print("Functional style: " + str(functional(15)))
    print("Declarative style: " + str(declarative(27)))
