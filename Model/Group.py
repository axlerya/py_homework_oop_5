from Model.Teacher import Teacher
from Model.Student import Student


class Group:
    """
    Класс, учебная группа (Преподаватель, Cтуденты, Название группы, ID группы)
    """

    def __init__(self, teacher: Teacher, id: int, name_group: str, student_list: list[Student]):
        self.__id = id
        self.__name_group = name_group
        self.__teacher = teacher
        self.__student_list = student_list

    @property
    def teacher(self):
        return self.__teacher

    @property
    def id(self):
        return self.__id

    @property
    def name_group(self):
        return self.__name_group

    @property
    def student_list(self):
        return self.__student_list

    @teacher.setter
    def teacher(self, teacher: Teacher):
        self.__teacher = teacher

    @id.setter
    def id(self, id: int):
        self.__id = id

    @name_group.setter
    def name_group(self, name_group: str):
        self.__name_group = name_group

    @student_list.setter
    def student_list(self, student_list: list[Student]):
        self.__student_list = student_list

    def __repr__(self):
        return f"""
Група: ID - {self.id} Название - {self.name_group}
{self.teacher}
Список студентов:
{self.student_list}
            """
