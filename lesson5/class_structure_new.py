import datetime


class Human3(object):
    total_count = 0

    def __new__(cls, *args, **kwargs):
        # Рахуватиму кожну народжену людину
        cls.total_count += 1
        instance = super(Human3, cls).__new__(Human3)
        return instance

    def __init__(self, name, surname, height, weight, birth_date):
        self.weight = weight
        self.name = name
        self.surname = surname
        self.height = height
        self.birth_date = birth_date


# Випробуймо програму
if __name__ == '__main__':
    ruslan = Human3("Руслан", "Закалюжний", 188, 87, datetime.date.today())
    print("Народився {} {}. Тепер нас уже {}".format(ruslan.name, ruslan.surname, Human3.total_count))

    maryna = Human3("Марина", "Гуляща", 135, 65, datetime.date.today())
    print("Народилася {} {}. Тепер нас уже {}".format(maryna.name, maryna.surname, Human3.total_count))
