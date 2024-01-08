"""
Tests des classes 'Contact' et 'AddressBook'.
"""
import unittest
from lib.contact import Contact
from lib.address_book import AddressBook


class TestContact(unittest.TestCase):
    """
Teste la classe Contact
    """
    def setUp(self):
        self.contact = Contact("Louis HUYBRECHTS", "louis@hotmail.com")

    def test_name_property(self):
        """
Teste la propriété name
        """
        self.assertEqual(self.contact.name, "Louis HUYBRECHTS")

    def test_empty_name(self):
        """
Teste la propriété name en cas de nom vide
        """
        with self.assertRaises(ValueError):
            self.contact = Contact("","nobody@gmail.com")

    def test_email_property(self):
        """
Teste la propriété email.
        """
        contact_test = Contact("Louis", 'a@b.fr')
        self.assertEqual(self.contact.email, "louis@hotmail.com")
        self.assertEqual(contact_test.email, "a@b.fr")

    def test_invalid_email(self):
        """
Teste la propriété mail en cas d'adresse email invalide.
        """
        with self.assertRaises(ValueError):
            self.contact = Contact("Louis","")
        with self.assertRaises(ValueError):
            self.contact = Contact("Louis","louis")
        with self.assertRaises(ValueError):
            self.contact = Contact("Louis","1ouis@mail.com")
        with self.assertRaises(ValueError):
            self.contact = Contact("Louis","louis@.com")
        with self.assertRaises(ValueError):
            self.contact = Contact("Louis","louis@mail.c")
        with self.assertRaises(ValueError):
            self.contact = Contact("Louis","louis@bobo.co3")
        with self.assertRaises(ValueError):
            self.contact = Contact("Louis","_ouis@bobo.com")
        with self.assertRaises(ValueError):
            self.contact = Contact("Louis","louis@3obo.com")
        with self.assertRaises(ValueError):
            self.contact = Contact("Louis","louis@_obo.com")

    def test_str(self):
        """
Teste la forme de chaîne de caractères.
        """
        expected_str = "Louis HUYBRECHTS - louis@hotmail.com"
        self.assertEqual(str(self.contact), expected_str)

    def test_repr(self):
        """
Teste la représentation.
        """
        expected_repr = "<Contact : Louis HUYBRECHTS - louis@hotmail.com>"
        self.assertEqual(repr(self.contact), expected_repr)

    def test_eq(self):
        """
Teste l'égalité entre 2 contacts.
        """
        contact_other = Contact("Martin CARPENTIER", "martin@gmail.be")
        contact_same = Contact("Louis HUYBRECHTS", "louis@hotmail.com")
        self.assertFalse(self.contact == contact_other )
        self.assertTrue(self.contact == contact_same)

class TestAddressBook(unittest.TestCase):
    """
Teste la classe AddressBook
    """
    def setUp(self):
        self.address_book = AddressBook()
        self.contact1 = Contact("Martin CARPENTIER", "martin@gmail.be")
        self.contact2 = Contact("Eve SOURIS", "eve@outlook.fr")
        self.contact3 = Contact("Simon SMEESTERS", "martin@student.gouv")
        self.contact4 = Contact("Alexia BOXHO", "alexia@yahoo.ch")

    def test_add_contact(self):
        """
Teste l'ajout d'un contact
        """
        self.assertEqual(len(self.address_book.contacts), 0)
        self.address_book.add_contact(self.contact1)
        self.assertEqual(len(self.address_book.contacts), 1)
        self.address_book.add_contact(self.contact2)
        self.assertEqual(len(self.address_book.contacts), 2)
        self.address_book.add_contact(self.contact3)
        self.assertEqual(len(self.address_book.contacts), 3)
        self.address_book.add_contact(self.contact4)
        self.assertEqual(len(self.address_book.contacts), 4)
        self.address_book.set_empty()

    def test_add_existing_contact(self):
        """
Teste l'ajout d'un contact déjà existant.
        """
        self.address_book.add_contact(self.contact1)
        with self.assertRaises(IndexError):
            same_name_contact = Contact("Martin CARPENTIER", "bubu@oui.be")
            self.address_book.add_contact(same_name_contact)

    def test_add_noncontact(self):
        """
Teste l'ajout d'un non-contact
        """
        with self.assertRaises(ValueError):
            self.address_book.add_contact(2)

    def test_str(self):
        """
Teste la forme de chaïne de caractères
        """
        self.assertEqual(str(self.address_book), "Annuaire vide")
        self.address_book.add_contact(self.contact2)
        self.assertEqual(str(self.address_book), f"Contacts dans l'annuaire:\n{self.contact2}")


    def test_get_contact_existing(self):
        """
Teste l'existence d'un contact dans l'annuaire.
        """
        self.address_book.add_contact(self.contact1)
        result = self.address_book.get_contact("Martin CARPENTIER")
        self.assertEqual(result, self.contact1)
        self.address_book.set_empty()

    def test_get_contact_nonexistent(self):
        """
Teste la non-existence d'un contact dans l'annuaire.
        """
        result = self.address_book.get_contact("chat")
        self.assertIsNone(result)

    def test_remove_contact_existing(self):
        """
Teste la suppression d'un contact.
        """
        self.address_book.add_contact(self.contact1)
        self.address_book.add_contact(self.contact2)
        self.assertEqual(len(self.address_book.contacts), 2)
        self.address_book.remove_contact("Eve SOURIS")
        self.assertEqual(len(self.address_book.contacts), 1)
        self.address_book.set_empty()

    def test_remove_contact_nonexistent(self):
        """
Teste la suppression d'un contact non-existant.
        """
        self.address_book.add_contact(self.contact1)
        self.assertEqual(len(self.address_book.contacts), 1)
        self.address_book.remove_contact("chat")
        self.assertEqual(len(self.address_book.contacts), 1)
        self.address_book.set_empty()


if __name__ == "__main__":
    unittest.main()