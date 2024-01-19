class User:
    """
    Класс, нужный для наследования другими классами, так как некоторые поля повторяются\n
    id - Уникальный номер\n
    surname - Фамилия\n
    name - Имя\n
    patronymic - Отчество 
    """

    def __init__(self, id: int, surname: str, name: str, patronymic: str):
        self.__id = id
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic

    @property
    def id(self):
        return self.__id

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @property
    def patronymic(self):
        return self.__patronymic

    @id.setter
    def id(self, id: int):
        self.__id = id

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @name.setter
    def name(self, name: str):
        self.__name = name

    @patronymic.setter
    def patronymic(self, patronymic: str):
        self.__patronymic = patronymic

    def __repr__(self):
        return f"ID: {self.id} Фамилия: {self.surname} Имя: {self.name} Отчество: {self.patronymic}"
