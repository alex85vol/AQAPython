from os.path import abspath, join

lst = list()

try:
    opened = open(abspath(join("fake_dir", "fake_file.txt")))
    lst = opened.readlines()
    opened.close()
except FileNotFoundError as e:
    print('File not found')
finally:
    print('Whenever it works')
