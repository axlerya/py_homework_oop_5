from Model.Student import Student
from Model.Teacher import Teacher
from Model.Group import Group
from Model.User import User
from Model.GroupService import GroupService


class DataService:
    """
        Класс хранящий информацию о всех пользователях и группах
    """
    _list_user = []

    def create_user(self, type: Student | Teacher, surname: str, name: str, patronymic: str):
        """ 
        Метод создающий пользователя  

        Args:
            type (Student | Teacher): тип объекта
            surname (str): фамилия
            name (str): имя
            patronymic (str): отчество
        """
        id = self.get_free_id_for_user(type)

        if type == Student:
            student = Student(id, surname, name, patronymic)
            self._list_user.append(student)

        if type == Teacher:
            teacher = Teacher(id, surname, name, patronymic)
            self._list_user.append(teacher)  
        
    def get_free_id_for_user(self, type: Student | Teacher ) -> int:
        """ Метод для получения не занятого уникального индификатора ( id )

        Args:
            type (Student | Teacher): тип данных

        Returns:
            int: уникальный индификатор ( ID )
        """
        max_id = 0
        current_id = 0
        
        for user in self._list_user:
            if type == Student and (isinstance(user, Student)):
                current_id = user.id

            if type == Teacher and (isinstance(user, Teacher)):
                current_id = user.id

            if (max_id < current_id):
                max_id = current_id
                    
        
        return max_id + 1

    def get_user_by_id(self, type: Student | Teacher, id: int) -> User | None:
        """Метод выполняет поиск пользователя по ID 

        Args:
            type (Student | Teacher): тип данных 
            id (int): ID пользователя

        Returns:
            User | None: Возвращает User или None, если пользователь не найден
        """
        for user in self._list_user:
            if type == Student and isinstance(user, Student) and user.id == id:
                return user

            if type == Teacher and isinstance(user, Teacher) and user.id == id:
                return user

        return None

    def get_all_users(self) -> list[User]:
        """Возвращает всех пользователей

        Returns:
            list[User]: список пользователей (type: User)
        """
        return self._list_user

    def get_all_students(self) -> list[Student]:
        """Возвращает всех студентов

        Returns:
            list[Student]: список студентов (type: Student)
        """
        student_list = []

        for student in self._list_user:
            if (isinstance(student, Student)):
                student_list.append(student)
        return student_list

    def get_all_teachers(self) -> list[Teacher]:
        """Возвращает всех преподавателей

        Returns:
            list[Teacher]: список преподавателей (type: Teacher)
        """
        teacher_list = []

        for teacher in self._list_user:
            if (isinstance(teacher, Teacher)):
                teacher_list.append(teacher)
        return teacher_list
