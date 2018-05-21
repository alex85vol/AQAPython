import pytest

from home_work.university.faculty import Faculty
from home_work.university.university import University


@pytest.fixture(scope="module")
def faculty_provider():
    faculties = list()
    faculties.append(Faculty.create_faculty())
    faculties.append(Faculty.create_faculty())
    return faculties


@pytest.fixture(scope="module")
def university_provider():
    return University.create_university()


def test_add_faculty(faculty_provider, university_provider):
    university_provider.add_faculty(faculty_provider[0])
    university_faculties_list = university_provider.university_faculties
    assert faculty_provider[0] in university_faculties_list


def test_delete_faculty(faculty_provider, university_provider):
    result = university_provider.delete_faculty(faculty_provider[0])
    university_faculties_list = university_provider.university_faculties
    assert result is True
    assert faculty_provider[0] not in university_faculties_list

def test_delete_faculty_negative(faculty_provider, university_provider):
    result = university_provider.delete_faculty(faculty_provider[1])
    assert result is False