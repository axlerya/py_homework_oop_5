from View.UserView import UserView
from Model.Student import Student


class StudentView(UserView):
    """
        Вспомогательный класс для вывода студентов в консоль
    """

    def send_in_console(self, students: list[Student] | Student):
        """Метод для вывода студентов в консоль

        Args:
            student (list[Student] | Student): список студентов ( type: Student ) или cтудент
        """
        try:
            for student in students:
                print(student)
        except:
            print(students)
