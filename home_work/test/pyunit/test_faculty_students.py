import unittest

from home_work.university.faculty import Faculty
from home_work.university.student import Student


class FacultyStudentsTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.student = Student.create_student()
        cls.foreign_student = Student.create_student()
        cls.faculty = Faculty.create_faculty()
        cls.students_list = list()

    @classmethod
    def tearDownClass(cls):
        del cls.faculty
        del cls.students_list
        del cls.student
        del cls.foreign_student

    def setUp(self):
        self.list_before_len = len(self.faculty.faculty_students)
        self.students_count_before = self.faculty.faculty_students_count

    def tearDown(self):
        pass

    def test_add_student(self):
        self.faculty.add_student(self.student)
        students_list = self.faculty.faculty_students
        students_count = self.faculty.faculty_students_count

        self.assertTrue(self.student in students_list,
                        "Student [{}] is not added to [{}]faculty".
                        format(self.student.name,
                               self.faculty.faculty_name))
        self.assertNotEquals(len(students_list), self.list_before_len,
                             "Students list length in [{}] faculty is not changed".format(self.faculty.faculty_name))
        self.assertTrue(students_count > self.students_count_before, "Count of faculty students is not increased")

    def test_delete_student(self):
        self.list_before_len = len(self.faculty.faculty_students)
        result = self.faculty.delete_student(self.student)
        students_list = self.faculty.faculty_students
        students_count = self.faculty.faculty_students_count

        self.assertTrue(result is True, "Student [{0}] is not deleted from [{1}]faculty".
                        format(self.student.name,
                               self.faculty.faculty_name))
        self.assertFalse(self.student in students_list,
                         "Student [{0}] is not deleted from [{1}]faculty".
                         format(self.student.name,
                                self.faculty.faculty_name))
        self.assertNotEquals(len(students_list), self.list_before_len,
                             "Students list length in [{}] faculty is not changed")
        self.assertTrue(students_count < self.students_count_before, "Faculty students count is not decreased")

    def test_delete_student_negative(self):
        result = self.faculty.delete_student(self.foreign_student)
        # with self.assertRaises(ValueError):
        #     self.faculty.delete_student(self.foreign_student)
        self.assertTrue(result is False, "Non faculty student is deleted")


if __name__ == '__main__':
    unittest.main()
