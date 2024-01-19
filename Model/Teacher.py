from Model.User import User


class Teacher(User):
    """
    Преподаватель наследник от User\n
    """

    def __init__(self, id, surname, name, patronymic):
        super().__init__(id, surname, name, patronymic)


    def __repr__(self):
        return f"Преподаватель - ID: {self.id} Фамилия: {self.surname} Имя: {self.name} Отчество: {self.patronymic}"
