from View.UserView import UserView
from Model.Teacher import Teacher


class TeacherView(UserView):
    """
        Вспомогательный класс для вывода перподавателей в консоль
    """
    def send_in_console(self, teachers: list[Teacher]):
        """Метод для вывода студентов в консоль

        Args:
            teachers (list[Teacher] | Teacher): список перподавателей ( type: Teacher ) или переподователя
        """
        try:
            for teacher in teachers:
                print(teacher)
        except:
            print(teachers)


