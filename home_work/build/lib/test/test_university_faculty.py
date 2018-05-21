import unittest

from faker import Faker

from home_work.university.university import University
from home_work.university.university import Faculty


class UniversityFacultiesTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fake = Faker()
        cls.faculty_01 = Faculty(cls.fake.company())
        cls.faculty_02 = Faculty('Faculty_02')
        cls.university = University('University_01')
