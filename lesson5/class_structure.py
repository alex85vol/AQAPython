from datetime import date


class Human2(object):

    def __init__(self, name, surname, height, weight, birth_date):
        self.name = name
        self.surname = surname
        self.height = height
        self.weight = weight
        self.birth_date = birth_date


john = Human2("John", "Walker", 195, 85, date(2000, 12, 15))

if __name__ == '__main__':
    print(john.name)
    print(john.birth_date)
