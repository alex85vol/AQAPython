import unittest

from home_work.university.faculty import Faculty
from home_work.university.university import University


class UniversityFacultiesTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.faculty_01 = Faculty.create_faculty()
        cls.faculty_02 = Faculty.create_faculty()
        cls.university = University.create_university()
        cls.students_count = int

    @classmethod
    def tearDown(cls):
        del cls.faculty_01
        del cls.faculty_02
        del cls.university
        del cls.students_count

    def setUp(self):
        self.len_faculties_before = len(self.university.university_faculties)

    def tearDown(self):
        pass

    def test_add_faculty(self):
        self.university.add_faculty(self.faculty_01)
        faculty_list = self.university.university_faculties

        self.assertTrue(self.faculty_01 in faculty_list, "Faculty [{0}] is not added to university [{1}]"
                        .format(self.faculty_01.faculty_name, self.university.university_name))
        self.assertTrue(len(faculty_list) > self.len_faculties_before,
                        "Faculties list length in [{}] university is not changed".format(
                            self.university.university_name))

    def test_delete_faculty(self):
        self.university.delete_faculty(self.faculty_01)
        faculty_list = self.university.university_faculties
        self.assertFalse(self.faculty_01 in faculty_list, "Faculty [{0}] is not removed from university [{1}]"
                         .format(self.faculty_01.faculty_name, self.university.university_name))
        self.assertTrue(len(faculty_list) < self.len_faculties_before,
                        "Faculties list length in [{}] university is not changed".format(
                            self.university.university_name))

    def test_delte_faculty_negative(self):
        result = self.university.delete_faculty(self.faculty_02)
        self.assertTrue(result is False, "Non university faculty is deleted")


if __name__ == '__main__':
    unittest.main()
