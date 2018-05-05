import os

name = "data.csv"
#new_name = "new_data.csv"


def get_directory():
    os.chdir("C:\PythonProject")


def read(number, opened_file):
    read_lines = []
    for i in range(number):
        read_lines.append(opened_file.readline())
    return read_lines


def open_file(file_name, mode):
    get_directory()
    return open(file_name, mode)


def get_data(file_name):
    source_file = open_file(file_name, "r")
    lines = read(2, source_file)
    items = lines.__getitem__(1).split('","')
    indexes = []
    for i in range(items.__len__()):
        if items.__getitem__(i).__contains__('WHO region') \
                | items.__getitem__(i).__contains__('Year') \
                | items.__getitem__(i).__contains__('Male') \
                | items.__getitem__(i).__contains__('Female'):
            indexes.append(i)
    count = source_file.readlines().__len__()
    source_file.close()
    return [count, indexes]


def create_list_by_indexed_elements(indexes_list):
    formed_list = []

    for index_to_select in indexes_list:
        formed_list.append(origin_list.__getitem__(index_to_select))
    return formed_list


def format_list(source_list):
    new_list = []
    for origin_item in source_list:
        changed_item = origin_item.strip('"') \
            .replace('/\/', '') \
            .replace('"\n', '') \
            .replace('"', '') \
            .strip()
        new_list.append(changed_item)
    return new_list


def filter_age(age_list, value):
    filtered_ages = list(filter(lambda age: float(age) > value, age_list))
    return filtered_ages


def form_result():
    formed_origin_list = create_list_by_indexed_elements(select_indexes)
    changed_list = format_list(formed_origin_list)
    name_list = changed_list[:2]
    value_list = changed_list[2:]
    values = list(filter(None, value_list))
    filtered_list = filter_age(values, 55)
    result = name_list + filtered_list
    return result


# def a():
#     file = open_file(name, "r")
#     new_file = open_file(new_name, "w")
#     print(file.readlines().__len__())
#     new_file.writelines(file.readlines())
#     file.close()
#     new_file.close()


if __name__ == "__main__":
    data = get_data(name)
    lines_count = data.__getitem__(0)
    select_indexes = data.__getitem__(1)
    file = open_file(name, "r")
    read(2, file)
    data_lines = read(lines_count, file)
    for i in range(lines_count):
        origin_list = data_lines.__getitem__(i).split('","')
        final_result = form_result()
        print(str(final_result))
