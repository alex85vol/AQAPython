def filter_using_for():
    filtered = list()
    for i in range(10):
        if i % 3 == 0:
            filtered.append(i)
    return filtered


def filter_using_filter():
    filtered = list(filter(lambda x: x % 3 == 0, range(10)))
    return filtered


if __name__ == "__main__":
    print('Filter using for :' + str(filter_using_for()))
    print('Filter using filter: ' + str(filter_using_filter()))
