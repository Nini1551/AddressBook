"""
Simulation d'un annuaire mail.
L'utilisateur peut ajouter ses contacts, représentés par leur mail et leur nom.
Il peut aussi consulter ses contacts.
Il peut rechercher un contact via son nom.
Il peut supprimer un contact.
Il peut quitter le programme.
"""
from lib.contact import Contact
from lib.address_book import AddressBook

def main():
    address_book = AddressBook()

    print("\nANNUAIRE : ")
    while True:
        print("1. Ajouter un contact")
        print("2. Afficher les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter\n")

        choice = input("Choisissez une option (1-5) : ")

        if choice == "1":
            name = input("Nom du contact : ")
            email = input("Email du contact : ")
            try:
                new_contact = Contact(name, email)
            except ValueError as error:
                print(f'Données invalides : {error}')
                continue
            try:
                address_book.add_contact(new_contact)
            except IndexError:
                print("Contact déjà existant dans l'annuaire !\n")
            print(f"Contact '{name}' ajouté avec succès!")

        elif choice == "2":
            print(f'\n{address_book.get_contacts()}\n')

        elif choice == "3":
            search_name = input("Entrez le nom du contact à rechercher: ")
            found_contact = address_book.get_contact(search_name)
            if found_contact:
                print(f"\nContact trouvé pour {search_name}: {found_contact}\n")
            else:
                print(f"\nAucun contact trouvé pour' {search_name}'\n")

        elif choice == "4":
            delete_name = input("\nEntrez le nom du contact à supprimer: ")
            address_book.remove_contact(delete_name)
            print(f"Contact '{delete_name}' supprimé avec succès!\n")

        elif choice == "5":
            print("\nAu revoir!")
            break

        else:
            print("\nChoix non valide. Veuillez choisir une option de 1 à 5.\n")

if __name__ == "__main__":
    main()