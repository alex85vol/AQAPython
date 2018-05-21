import random

from home_work.university.name_data import NameData


class Student(object):

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @classmethod
    def create_student(cls):
        genders = ['Male', 'Female']
        gender = random.choice(genders)
        return Student(NameData.STUDENT_NAME.value if gender is 'Male' else NameData.STUDENT_FEMALE_NAME.value,
                       random.randint(18, 30),
                       gender)

    @staticmethod
    def global_students_list():
        global_list = list()
        for i in range(30):
            global_list.append(Student.create_student())
        return global_list
