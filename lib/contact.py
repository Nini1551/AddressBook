"""
Contact représenté par son nom et son email.
"""
import re


class Contact:
    """
Contact représenté par son nom et son email.
    """
    EMAIL_REGEX = r"^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z][a-zA-Z0-9.-]*\.[a-zA-Z]{2,}$"

    def __init__(self, name: str, email: str):
        """
Initialise un contact
PRE : - name : nom d'un contact avec au moins un caractère
      - email : email valide
        Un email est valide si :
        - Il commence par au moins une lettre suivis de n'importe quels caractères non-arobase.
        - La partie de départ est suivi d'une arobase.
        - L'arobase est suivi d'un moins une lettre suivie de lettres, de chiffres, de points ou de trémas
        - La partie précédente est suivie d'un point.
        - Il finit par au moins deux lettres.
POST : Initialise les attributs suivants :
       - name : nom du contact
       - email : adresse email du contact
RAISES : - ValueError : Si le nom ou le mail est invalide.
        """
        if not self.is_valid_name(name):
            raise ValueError("Name cannot be empty")

        if not self.is_valid_email(email):
            raise ValueError("Email is not valid")

        self.__name = name
        self.__email = email

    @property
    def name(self) -> str:
        """
Propriété name du contact
PRE : -
POST : Renvoie le nom du contact
        """
        return self.__name

    @property
    def email(self) -> str:
        """
Propriété email du contact
PRE : -
POST : Renvoie l'adresse email du contact.
        """
        return self.__email

    @staticmethod
    def is_valid_name(name) -> bool:
        """
Indique si la valeur est un nom valide
PRE : - name : une chaîne de caractères
POST : Renvoie si la chaîne de caractères est un nom valide.
       Un nom est valide s'il comporte au moins un caractère.
        """
        return bool(name)

    @staticmethod
    def is_valid_email(email) -> bool:
        """
Indique si la valeur est une adresse mail valide.
PRE : - email : une chaîne de caractères
POST : Renvoie si la chaïne de caractères est une adresse mail valide.
       Un email est valide si :
       - Il commence par au moins une lettre suivie de n'importe quels caractères non-arobase.
       - La partie de départ est suivi d'une arobase.
       - L'arobase est suivi d'un moins une lettre suivie de lettres, de chiffres, de points ou de trémas
       - La partie précédente est suivie d'un point.
       - Il finit par au moins deux lettres.
        """
        return bool(re.match(Contact.EMAIL_REGEX, email))

    def __str__(self) -> str:
        """
Forme sous chaîne de caractères du contact
PRE : -
POST : Le nom du contact et le mail du contact séparés par ' - '.
        """
        return f'{self.name} - {self.email}'

    def __repr__(self) -> str:
        """
Représentation du contact
PRE : -
POST : '<Contact : **contact**>' où contact est la forme sous chaîne de caractères du contact.
        """
        return f'<Contact : {self}>'

    def __eq__(self, other):
        """
Vérifie l'égalité de deux contacts
PRE : - other : un autre contact
POST : Deux contacts sont égaux si leur forme sous chaîne de caractères sont les memes.
        """
        return str(self) == str(other)
