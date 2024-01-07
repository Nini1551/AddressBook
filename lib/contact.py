class Contact:
    def __init__(self, name: str, email: str):
        self.__name = name
        self.__email = email

    @property
    def name(self) -> str:
        return self.__name

    @property
    def email(self) -> str:
        return self.__email

    def __str__(self) -> str:
        return f'{self.name} - {self.email}'

    def __repr__(self) -> str:
        return f'<Contact : {self}>'
