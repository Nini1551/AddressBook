from lib.address_book import AddressBook
from lib.contact import Contact
import sys


class CLIApp:
    def __init__(self):
        self.address_book = AddressBook()

    @staticmethod
    def get_options_menu():
        options_menu = "ANNUAIRE : \n"
        options_menu += "1. Ajouter un contact\n"
        options_menu += "2. Afficher les contacts\n"
        options_menu += "3. Rechercher un contact\n"
        options_menu += "4. Supprimer un contact\n"
        options_menu += "5. Quitter"

        return options_menu

    def run(self):
        while True:
            print(f"\n{CLIApp.get_options_menu()}\n")
            choice = input("Choisissez une option (1-5) : ")

            if choice == "1":
                self.add_contact()

            elif choice == "2":
                self.display_contacts()

            elif choice == "3":
                self.search_contact()

            elif choice == "4":
                self.delete_contact()

            elif choice == "5":
                self.quit()

            else:
                print("\nChoix non valide. Veuillez choisir une option de 1 à 5.\n")

    def add_contact(self):
        name = input("Nom du contact : ")
        email = input("Email du contact : ")
        try:
            new_contact = Contact(name, email)
            self.address_book.add_contact(new_contact)
            print(f"Contact '{name}' ajouté avec succès!")
        except ValueError as error:
            print(f'Données invalides : {error}')
        except IndexError:
            print("Contact déjà existant dans l'annuaire !\n")

    def display_contacts(self):
        print(f'\n{self.address_book.get_contacts()}\n')

    def search_contact(self):
        search_name = input("Entrez le nom du contact à rechercher: ")
        found_contact = self.address_book.get_contact(search_name)
        if found_contact:
            print(f"\nContact trouvé pour {search_name}: {found_contact}\n")
        else:
            print(f"\nAucun contact trouvé pour '{search_name}'\n")

    def delete_contact(self):
        delete_name = input("\nEntrez le nom du contact à supprimer: ")
        found_contact = self.address_book.get_contact(delete_name)
        if found_contact:
            self.address_book.remove_contact(delete_name)
            print(f"Contact '{delete_name}' supprimé avec succès!\n")
        else:
            print(f"Aucun contact trouvé pour' {delete_name}'\n")

    def quit(self):
        print("\nAu revoir!")
        sys.exit(0)


if __name__ == "__main__":
    cli = CLIApp()
    cli.run()
