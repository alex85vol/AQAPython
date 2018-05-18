import unittest

from home_work.faculty import Faculty
from home_work.student import Student


class FacultyStudentsTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.student = Student.create_student()
        cls.foreign_student = Student.create_student()
        cls.faculty = Faculty("Test_faculty")
        cls.students_list = list()
        cls.students_count = int

    @classmethod
    def tearDownClass(cls):
        del cls.faculty
        del cls.students_list
        del cls.students_count
        del cls.student
        del cls.foreign_student

    def setUp(self):
        self.list_before_len = len(self.faculty.faculty_students)

    def tearDown(self):
        pass

    def test_add_student(self):
        self.faculty.add_student(self.student)
        students_list = self.faculty.faculty_students

        self.assertTrue(students_list.__contains__(self.student),
                        "Student [{} {} {}] is not added to [{}]faculty".
                        format(self.student.name, self.student.surname, self.student.middle_name,
                               self.faculty.faculty_name))
        self.assertNotEquals(len(students_list), self.list_before_len,
                             "Students list length in [{}] faculty is not changed")

    def test_delete_student(self):
        self.list_before_len = len(self.faculty.faculty_students)
        result = self.faculty.delete_student(self.student)
        students_list = self.faculty.faculty_students

        self.assertTrue(result is True, "Student [{} {} {}] is not deleted from [{}]faculty".
                        format(self.student.name, self.student.surname, self.student.middle_name,
                               self.faculty.faculty_name))
        self.assertFalse(students_list.__contains__(self.student),
                         "Student [{} {} {}] is not deleted from [{}]faculty".
                         format(self.student.name, self.student.surname, self.student.middle_name,
                                self.faculty.faculty_name))

    def test_delete_student_negative(self):
        result = self.faculty.delete_student(self.foreign_student)
        # with self.assertRaises(ValueError):
        #     self.faculty.delete_student(self.foreign_student)
        self.assertTrue(result is False, "Non faculty student is deleted")


if __name__ == '__main__':
    unittest.main()
