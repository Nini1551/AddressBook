import re

class Contact:
    email_regex = r"^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z][a-zA-Z0-9.-]*\.[a-zA-Z]{2,}$"

    def __init__(self, name: str, email: str):
        if len(name) < 1:
            raise ValueError("Name cannot be empty")

        if not re.match(self.email_regex, email):
            raise ValueError("Email is not valid")

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

    def __eq__(self, other):
        return str(self) == str(other)
