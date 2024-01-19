from Model.Group import Group


class GroupView:
    """
        Вспомогательный класс для вывода учебной групп в консоль 
    """
    def send_in_console(self, group: list[Group] | Group):
        """Вывод в групп в консоль

        Args:
            list (list[Group] | Group): список групп ( type: Group) или группа
        """
        try:
            for groups in group:
                print(groups)
        except:
            print(group)
