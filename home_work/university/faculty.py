from home_work.university.name_data import NameData


class Faculty(object):

    def __init__(self, faculty_name):
        self.faculty_name = faculty_name
        self.faculty_students = list()

    @property
    def faculty_students_count(self):
        return len(self.faculty_students)

    def add_student(self, student):
        self.faculty_students.append(student)

    def delete_student(self, student):
        try:
            self.faculty_students.remove(student)
            is_deleted = True
        except RuntimeError:
            print('Student [{0}] is not deleted from faculty [{1}]'.format
                  (student.name, self.faculty_name))
            is_deleted = False
        except ValueError:
            print('Student [{0}] is not found in faculty [{1}]'.format
                  (student.name, self.faculty_name))
            is_deleted = False

        return is_deleted

    @staticmethod
    def create_faculty():
        return Faculty(NameData.FACULTY_NAME.value)


