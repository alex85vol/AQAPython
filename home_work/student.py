import random

import names


class Student(object):

    def __init__(self, name, surname, middle_name, age, sex):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.age = age
        self.sex = sex

    @staticmethod
    def create_student():
        genders = ['Male', 'Female']
        gender = random.choice(genders)
        return Student(names.get_first_name(gender),
                       names.get_full_name(gender)[:5],
                       names.get_full_name(gender)[:6],
                       random.randint(18, 30),
                       gender)

    @staticmethod
    def global_students_list():
        global_list = list()
        for i in range(30):
            global_list.append(Student.create_student())
        return global_list


test = Student

if __name__ == '__main__':
    test.global_students_list()
