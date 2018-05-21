import pytest

from home_work.university.faculty import Faculty
from home_work.university.student import Student


@pytest.fixture(scope="module")
def student_provider():
    students = list()
    students.append(Student.create_student())
    students.append(Student.create_student())
    return students


@pytest.fixture(scope="module")
def faculty_provider():
    return Faculty.create_faculty()


def test_add_student(student_provider, faculty_provider):
    faculty_provider.add_student(student_provider[0])
    faculty_students_list = faculty_provider.faculty_students
    assert student_provider[0] in faculty_students_list


def test_remove_student(student_provider, faculty_provider):
    result = faculty_provider.delete_student(student_provider[0])
    faculty_students_list = faculty_provider.faculty_students
    assert result is True
    assert student_provider[0] not in faculty_students_list


def test_remove_student_negative(student_provider, faculty_provider):
    result = faculty_provider.delete_student(student_provider[1])
    assert result is False
