from home_work_2.faculties import Math, Sociology, Chemistry, Medicine


class Universities(object):
    faculty_list = [Math, Sociology, Chemistry, Medicine]

    @classmethod
    def get(cls, name, students_list):
        faculties = Universities.faculty_list
        for faculty in faculties:
            students = faculty.faculty_students
            for student in students:
                if student.university is name:
                    students_list.append(student)


class Michigan(Universities):
    total_count = 0
    name = 'Michigan'
    students_list = list()

    @classmethod
    def get_info(cls):
        Universities.get(cls.name, cls.students_list)
        print('Total count of students in [{0}] university is [{1}]'.format(cls.name, len(cls.students_list)))


class Oxford(Universities):
    total_count = 0
    name = 'Oxford'
    students_list = list()

    @classmethod
    def get_info(cls):
        Universities.get(cls.name, cls.students_list)
        print('Total count of students in [{0}] university is [{1}]'.format(cls.name, len(cls.students_list)))


class Priston(Universities):
    total_count = 0
    name = 'Priston'
    students_list = list()

    @classmethod
    def get_info(cls):
        Universities.get(cls.name, cls.students_list)
        print('Total count of students in [{0}] university is [{1}]'.format(cls.name, len(cls.students_list)))


class Elle(Universities):
    total_count = 0
    name = 'Elle'
    students_list = list()

    @classmethod
    def get_info(cls):
        Universities.get(cls.name, cls.students_list)
        print('Total count of students in [{0}] university is [{1}]'.format(cls.name, len(cls.students_list)))


if __name__ == '__main__':
    Michigan.get_info()
    Oxford.get_info()
    Priston.get_info()
    Elle.get_info()
