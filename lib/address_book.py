"""
Annuaire mail regroupant des contacts.
Les contacts sont représentés par leur nom et leur email.
"""
from lib.contact import Contact


class AddressBook:
    """
Annuaire mail regroupant des contacts.
Les contacts sont représentés par leur nom et leur email.
    """
    def __init__(self):
        """
Initialise un annuaire mail.
PRE : -
POST : Initialise les attributs suivants :
       - contacts : liste des contacts
         Initialisée à vide
        """
        self.contacts = []

    def __str__(self) -> str:
        """
Forme sous chaîne de caractères.
PRE : -
POST : La forme sous chaîne de caractères de la liste de contacts
        """
        return str(self.contacts)

    def __repr__(self) -> str:
        """
Représentation de l'annuaire mail.
PRE : -
POST : '<AddressBook : **contacts**>' où contacts est la forme sous chaîne de caractères de l'annuaire.
        """
        return f'<AddressBook : {self}>'

    def get_contacts(self) -> str:
        """
Fournit l'annuaire mail des contacts.
PRE : -
POST : Indique si l'annuaire est vide.
       'Contact dans l'annuaire :' suivi d'un passage à la ligne
       ainsi que chacun des contacts séparés par des retours à la ligne.
        """
        if len(self.contacts) == 0:
            return 'Annuaire vide'
        annuaire = "Contacts dans l'annuaire:\n"
        annuaire += '\n'.join(map(lambda x: str(x), self.contacts))
        return annuaire

    def add_contact(self, contact: Contact):
        """
Ajoute un contact dans l'annuaire.
PRE : - contact : un contact valide
POST : Ajoute le contact dans l'annuaire à la fin de celui-ci.
RAISES : - ValueError : la valeur ajoutée n'est pas un contact.
         - IndexError : le contact a un nom déjà présent dans l'annuaire.
        """
        if not isinstance(contact, Contact):
            raise ValueError('Value added is not a contact')

        if self.get_contact(contact.name):
            raise IndexError('There is already a contact with that name')

        self.contacts.append(contact)

    def get_contact(self, name: str) -> Contact | None:
        """
Trouve si un contact est dans l'annuaire.
PRE : - name : nom d'un contact présent dans l'annuaire.
POST : Renvoie le contact ayant le nom indiqué.
       Renvoie None s'il n'y a pas de contacts avec ce nom dans l'annuaire.
        """
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def remove_contact(self, name: str):
        """
Retire un contact de l'annuaire.
PRE : - name : nom d'un contact présent dans l'annuaire.
POST : Retire le contact ayant le nom indiqué de l'annuaire.
       S'il n'y a pas de contacts avec ce nom dans l'annuaire, ne fais rien.
        """
        contact = self.get_contact(name)
        if contact:
            self.contacts.remove(contact)

    def set_empty(self):
        """
Vide l'annuaire.
PRE : -
POST : Initialise la liste de contacts à vide.
        """
        self.contacts = []
