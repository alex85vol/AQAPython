import random

import names


class Students(object):
    global_list = list()

    def __init__(self, name, surname, middle_name, age, sex, faculty, university):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.age = age
        self.sex = sex
        self.faculty = faculty
        self.university = university

    @classmethod
    def university_list(cls):
        return ['Michigan', 'Oxford', 'Priston', 'Elle']

    @classmethod
    def faculties_list(cls):
        return ['Math', 'Sociology', 'Chemistry', 'Medicine']

    @classmethod
    def create_student(cls):
        genders = ['Male', 'Female']
        gender = random.choice(genders)
        faculties = cls.faculties_list()
        student_faculty = random.choice(faculties)
        universities = cls.university_list()
        student_university = random.choice(universities)
        return Students(names.get_first_name(gender),
                        names.get_full_name(gender)[:5],
                        names.get_full_name(gender)[:6],
                        random.randint(18, 30),
                        gender,
                        student_faculty,
                        student_university)

    @classmethod
    def global_students_list(cls):
        if len(cls.global_list) == 0:
            for i in range(400):
                cls.global_list.append(Students.create_student())
        return cls.global_list

