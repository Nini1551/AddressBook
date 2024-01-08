"""
Simulation d'un annuaire mail.
L'utilisateur peut ajouter ses contacts, représentés par leur mail et leur nom.
Il peut aussi consulter ses contacts.
Il peut rechercher un contact via son nom.
Il peut supprimer un contact.
Il peut quitter le programme.
"""
from cli import CLIApp

def main():
    cli = CLIApp()
    cli.run()

if __name__ == "__main__":
    main()