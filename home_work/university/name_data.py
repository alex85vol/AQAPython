from enum import Enum

from faker import Faker


class NameData(Enum):
    faker = Faker()

    STUDENT_NAME = faker.name()

    STUDENT_FEMALE_NAME = faker.name_female()

    FACULTY_NAME = faker.company()

    UNIVERSITY_NAME = faker.state()




