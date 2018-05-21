from functools import reduce

from home_work.university.name_data import NameData


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

    @staticmethod
    def create_university():
        return University(NameData.UNIVERSITY_NAME.value)
