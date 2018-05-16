from home_work_2.students import Students


class Faculties(object):

    @classmethod
    def add(cls, faculty_name, faculty_students):
        global_students_list = Students.global_students_list()
        for student in global_students_list:
            if student.faculty is faculty_name:
                faculty_students.append(student)
        return len(faculty_students)

    @classmethod
    def remove(cls, faculty_students):
        len_before = len(faculty_students)
        list.pop(faculty_students)
        cls.students_count = len(faculty_students)
        return len_before is not len(faculty_students)


class Math(Faculties):
    students_count = 0
    faculty_name = 'Math'
    faculty_students = list()

    @classmethod
    def add_student(cls):
        cls.students_count = Faculties.add(cls.faculty_name, cls.faculty_students)
        print('Total count of students on [{0}] faculty is [{1}]'.format(cls.faculty_name, cls.students_count))

    @classmethod
    def remove_student(cls):
        is_deleted = Faculties.remove(cls.faculty_students)
        if is_deleted is True:
            cls.students_count = len(cls.faculty_students)
        return is_deleted


class Sociology(Faculties):
    students_count = 0
    faculty_name = 'Sociology'
    faculty_students = list()

    @classmethod
    def add_student(cls):
        cls.students_count = Faculties.add(cls.faculty_name, cls.faculty_students)
        print('Total count of students on [{0}] faculty is [{1}]'.format(cls.faculty_name, cls.students_count))

    @classmethod
    def remove_student(cls):
        is_deleted = Faculties.remove(cls.faculty_students)
        if is_deleted is True:
            cls.students_count = len(cls.faculty_students)
        return is_deleted


class Chemistry(Faculties):
    students_count = 0
    faculty_name = 'Chemistry'
    faculty_students = list()

    @classmethod
    def add_student(cls):
        cls.students_count = Faculties.add(cls.faculty_name, cls.faculty_students)
        print('Total count of students on [{0}] faculty is [{1}]'.format(cls.faculty_name, cls.students_count))

    @classmethod
    def remove_student(cls):
        is_deleted = Faculties.remove(cls.faculty_students)
        if is_deleted is True:
            cls.students_count = len(cls.faculty_students)
        return is_deleted


class Medicine(Faculties):
    students_count = 0
    faculty_name = 'Medicine'
    faculty_students = list()

    @classmethod
    def add_student(cls):
        cls.students_count = Faculties.add(cls.faculty_name, cls.faculty_students)
        print('Total count of students on [{0}] faculty is [{1}]'.format(cls.faculty_name, cls.students_count))

    @classmethod
    def remove_student(cls):
        is_deleted = Faculties.remove(cls.faculty_students)
        if is_deleted is True:
            cls.students_count = len(cls.faculty_students)
        return is_deleted


print('Total count of students is [{}]'.format(len(Students.global_students_list())))
Math.add_student()
Sociology.add_student()
Chemistry.add_student()
Medicine.add_student()
