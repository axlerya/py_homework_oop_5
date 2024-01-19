from Model.Group import Group
from Model.Student import Student
from Model.Teacher import Teacher


class GroupService:
    """
    Класс для формирования учебной группы
    """
    _list_group = []

    def create_group(self, teacher: Teacher, student_list: list[Student], name_group: str) -> Group:
        """Создает учебную группу

        Args:
            teacher (Teacher): преподаватель
            student_list (list[Student]): список студентов
            name_group (str): название группы
            id_group (int): id группы

        Returns:
            Group: Возращает экземпляр класса Group
        """
        id = self.get_free_id_for_group(Group)
        group = Group(teacher, id, name_group, student_list)
        self._list_group.append(group)
        return group

    def get_all_student_groups(self) -> list[Group]:
        """Возвращает все группы

        Returns:
            list[Group]: список групп ( type: Group )
        """
        return self._list_group
    
    def get_group_by_id(self, type: Group, id: int) -> Group | None:
        """Возваращет группу по id

        Args:
            type (Group): тип данных
            id (int): id группы

        Returns:
            Group | None: группа студентов ( type: Group ) | None если группы не найдена
        """
        for group in self._list_group:
            if type == Group and isinstance(group, Group) and group.id == id:
                return group
        return None

    def get_free_id_for_group(self, type: Group) -> int:
        """Возвращает чистый id для создания группы

        Args:
            type (Group): тип данных

        Returns:
            int: чистый id
        """
        max_id = 0
        current_id = 0

        for group in self._list_group:
            if type == Group and (isinstance(group, Group)):
                current_id = group.id

            if (max_id < current_id):
                max_id = current_id

        return max_id + 1
