from lib.contact import Contact


class AddressBook:
    def __init__(self):
        self.contacts = []

    def __str__(self) -> str:
        if len(self.contacts) == 0:
            return 'Annuaire vide'
        annuaire = "Contacts dans l'annuaire:\n"
        annuaire += '\n'.join(map(lambda x: str(x), self.contacts))
        return annuaire

    def add_contact(self, contact: Contact):
        if self.get_contact(contact.name):
            raise ValueError('There is already a contact with that name')
        self.contacts.append(contact)

    def get_contact(self, name: str) -> Contact | None:
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def remove_contact(self, name: str):
        contact = self.get_contact(name)
        if contact:
            self.contacts.remove(contact)

    def set_empty(self):
        self.contacts = []
