from functools import reduce

from home_work.university.faculty import Faculty
from home_work.university.student import Student


class University(object):

    def __init__(self, university_name):
        self.university_name = university_name
        self.university_faculties = list()

    @property
    def university_students_count(self):
        return reduce(lambda x, y: x + y, list(map(lambda x: x.faculty_students_count, self.university_faculties)))

    def add_faculty(self, faculty):
        self.university_faculties.append(faculty)

    def delete_faculty(self, faculty):
        try:
            self.university_faculties.remove(faculty)
            is_deleted = True
        except RuntimeError:
            print('Faculty [{0}] is not deleted from university'.format(faculty.faculty_name))
            is_deleted = False
        except ValueError:
            print('Faculty [{0}] is not found in university'.format(faculty.faculty_name))
            is_deleted = False
        return is_deleted


if __name__ == '__main__':
    student_01 = Student.create_student()
    student_02 = Student.create_student()
    student_03 = Student.create_student()
    student_04 = Student.create_student()
    student_05 = Student.create_student()
    student_06 = Student.create_student()
    student_07 = Student.create_student()
    student_08 = Student.create_student()
    student_09 = Student.create_student()
    student_10 = Student.create_student()

    faculty_01 = Faculty('Math')
    faculty_02 = Faculty('Sociology')
    faculty_03 = Faculty('Chemistry')
    faculty_04 = Faculty('Test faculty')

    faculty_01.add_student(student_01)
    faculty_01.add_student(student_02)
    faculty_01.add_student(student_03)

    faculty_02.add_student(student_04)
    faculty_02.add_student(student_05)
    faculty_02.add_student(student_06)

    faculty_03.add_student(student_07)
    faculty_03.add_student(student_08)
    faculty_03.add_student(student_09)

    university_01 = University('Michigan')
    university_02 = University('Preston')
    university_03 = University('Elle')

    university_01.add_faculty(faculty_01)
    university_01.add_faculty(faculty_02)
    university_01.add_faculty(faculty_03)

    university_02.add_faculty(faculty_02)
    university_02.add_faculty(faculty_03)

    university_03.add_faculty(faculty_01)
    university_03.add_faculty(faculty_03)

    print('Students count on [{0}] faculty is [{1}]'
          .format(faculty_01.faculty_name, faculty_01.faculty_students_count))
    print('Students count on [{0}] faculty is [{1}]'
          .format(faculty_02.faculty_name, faculty_02.faculty_students_count))
    print('Students count on [{0}] faculty is [{1}]'
          .format(faculty_03.faculty_name, faculty_03.faculty_students_count))

    print('Students count in [{0}] university is [{1}]'
          .format(university_01.university_name, university_01.university_students_count))
    print('Students count in [{0}] university is [{1}]'
          .format(university_02.university_name, university_02.university_students_count))
    print('Students count in [{0}] university is [{1}]'
          .format(university_03.university_name, university_03.university_students_count))
    faculty_01.delete_student(student_10)
    faculty_01.delete_student(student_04)
    faculty_01.delete_student(student_01)

    faculty_02.delete_student(student_10)
    faculty_02.delete_student(student_01)
    faculty_02.delete_student(student_04)

    faculty_03.delete_student(student_10)
    faculty_03.delete_student(student_02)
    faculty_03.delete_student(student_08)

    university_01.delete_faculty(faculty_04)
    university_01.delete_faculty(faculty_01)

    university_02.delete_faculty(faculty_04)
    university_02.delete_faculty(faculty_01)
    university_02.delete_faculty(faculty_02)

    university_03.delete_faculty(faculty_04)
    university_03.delete_faculty(faculty_02)
    university_03.delete_faculty(faculty_01)
