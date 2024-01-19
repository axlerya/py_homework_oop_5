from Model.User import User


class Student(User):
    """
    Класс наследник от User
    """

    def __init__(self, id: int, surname: str, name: str, patronymic: str):
        super().__init__(id, surname, name, patronymic)

    def __repr__(self):
        return f"Студент - ID: {self.id} Фамилия: {self.surname} Имя: {self.name} Отчество: {self.patronymic}"
