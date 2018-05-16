import heapq
import os

name = "data.csv"


def get_directory():
    os.chdir("C:\PythonProject")


def open_file(file_name, mode):
    get_directory()
    return open(file_name, mode)


def get_data(file_name):
    source_file = open_file(file_name, "r")
    lines = source_file.readlines()[2:]
    items = list(map(lambda x: x.split('","')[:3], lines))
    return items


def get_leaders(data_list):
    names = list(map(lambda x: x[0].strip('"') + ' ' + x[1].strip('"'), data_list))
    values = list(map(lambda y: y[2], data_list))
    dictionary = dict(zip(names, values))
    leader_names = heapq.nlargest(3, dictionary, key=dictionary.get)
    leader_values = list(map(lambda z: dictionary.get(z), leader_names))
    return dict(zip(leader_names, leader_values))


if __name__ == "__main__":
    print(str(get_leaders(get_data(name))))
