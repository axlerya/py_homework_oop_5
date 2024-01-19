from Model.DataService import DataService
from Model.GroupService import GroupService
from View.GroupView import GroupView
from View.StudentView import StudentView
from View.TeacherView import TeacherView
from Model.Student import Student
from Model.Teacher import Teacher
from Model.Group import Group


class Controller:
    """
    Класс в котором описанно связь между Model и View для дальнейшего использования в клиентском коде 
    """

    _data_service = DataService()
    _group_view = GroupView()
    _stundent_group_service = GroupService()
    _student_view = StudentView()
    _teacher_view = TeacherView()

    def create_student(self, type: Student, surname: str, name: str, patronymic: str):
        """Метод создающий студента

        Args:
            type (Student): тип данных 
            surname (str): фамилия 
            name (str): имя 
            patronymic (str): отчество
        """
        self._data_service.create_user(type, surname, name, patronymic)

    def create_teacher(self, type: Teacher, surname: str, name: str, patronymic: str):
        """Метод создающий учителя

        Args:
            type (Teacher): тип данных 
            surname (str): фамилия 
            name (str): имя 
            patronymic (str): отчество
        """
        self._data_service.create_user(type, surname, name, patronymic)

    def get_all_student(self):
        """Выводит всех студентов в консоль

        Returns:
            list[Student]: список студентов (type: Student) в консоль
        """
        self._student_view.send_in_console(self._data_service.get_all_students())
        
    def get_all_teacher(self):
        """Выводит всех преподавателей в консоль

        Returns:
            list[Teacher]: список преподавателей (type: Teacher) в консоль
        """
        self._teacher_view.send_in_console(self._data_service.get_all_teachers())
        
    def get_user_by_id(self, type: Student | Teacher, id: int):
        """Возвращает пользователя по ID в консоль

        Args:
            type (Student | Teacher): тип данных
            id (int): id для поиска
        """
        if type == Teacher:
            self._teacher_view.send_in_console(self._data_service.get_user_by_id(type,id))
        if type == Student:
            self._student_view.send_in_console(self._data_service.get_user_by_id(type, id))
            

    def get_group_by_id(self, id: int):
        """Возвращает группу по ID в консоль

        Args:
            id (int): id для поиска
        """
        self._group_view.send_in_console(self._stundent_group_service.get_group_by_id(Group,id))
        
    def create_student_group(self, teacher_id: int, student_id_list: list[int], name_group: str):
        """Создает группу по ID
        
        Args:
            teacher_id (int): ID преподавателя
            student_id_list (list[int]): список с ID студентов
            name_group (str): наименование группы
        """
        teacher = self._data_service.get_user_by_id(Teacher, teacher_id)
        student_list = []
        for id in student_id_list:
            student_list.append(self._data_service.get_user_by_id(Student, id))
            
        self._stundent_group_service.create_group(teacher, student_list, name_group)
        
    def get_all_student_group(self):
        """Выводит все учебные группы в консоль

        Returns:
            list[Group]: список групп ( type: Group ) в консоль
        """
        self._group_view.send_in_console(self._stundent_group_service.get_all_student_groups())
        