class Student(object):

    def __init__(self, name, surname, age, faculty):
        self.name = name
        self.surname = surname
        self.age = age
        self.faculty = faculty


class University(object):
    students_count = 0

    def __new__(cls, *args, **kwargs):
        cls.students_count += 1
        instance = cls.students_count
        return instance


if __name__ == '__main__':
    student1 = Student('John', 'Smith', 28, 'Philosophy')
    student2 = Student('Alex', 'Jonson', 24, 'Chemistry')
    print(University.students_count)


