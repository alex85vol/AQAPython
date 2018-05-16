from datetime import date


class Humanoid(object):
    def __init__(self, name, surname, date_of_the_birth):
        self.name = name
        self.surname = surname
        self.date_of_the_birth = date_of_the_birth

    @property
    def age(self):
        return (date.today() - self.date_of_the_birth).days / 365
    

leska = Humanoid('Jane', 'Twerty', date(1914, 1, 1))

if __name__ == '__main__':
    print(leska.age)
