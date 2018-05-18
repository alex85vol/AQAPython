import unittest

from faker import Faker

from home_work.faculty import Faculty
from home_work.university import University


class UniversityFacultiesTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fake = Faker()
        cls.faculty_01 = Faculty(cls.fake.state)
        cls.faculty_02 = Faculty('Faculty_02')
        cls.university = University('University_01')
