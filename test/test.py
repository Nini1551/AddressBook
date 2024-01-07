import unittest
from lib.contact import Contact
from lib.address_book import AddressBook


class TestContact(unittest.TestCase):
    def setUp(self):
        self.contact = Contact("Louis HUYBRECHTS", "louis@hotmail.com")

    def test_name_property(self):
        self.assertEqual(self.contact.name, "Louis HUYBRECHTS")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            self.contact = Contact("","nobody@gmail.com")

    def test_email_property(self):
        contact_test = Contact("Louis", 'a@b.fr')
        self.assertEqual(self.contact.email, "louis@hotmail.com")
        self.assertEqual(contact_test.email, "a@b.fr")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            self.contact = Contact("Louis","")
            self.contact = Contact("Louis","louis")
            self.contact = Contact("Louis","1ouis@mail.com")
            self.contact = Contact("Louis","louis@.com")
            self.contact = Contact("Louis","louis@mail.c")
            self.contact = Contact("Louis","louis@bobo.co3")
            self.contact = Contact("Louis","_ouis@bobo.com")
            self.contact = Contact("Louis","louis@3obo.com")
            self.contact = Contact("Louis","louis@_obo.com")

    def test_str(self):
        expected_str = "Louis HUYBRECHTS - louis@hotmail.com"
        self.assertEqual(str(self.contact), expected_str)

    def test_repr(self):
        expected_repr = "<Contact : Louis HUYBRECHTS - louis@hotmail.com>"
        self.assertEqual(repr(self.contact), expected_repr)

    def test_eq(self):
        contact_other = Contact("Martin CARPENTIER", "martin@gmail.be")
        contact_same = Contact("Louis HUYBRECHTS", "louis@hotmail.com")
        self.assertFalse(self.contact == contact_other )
        self.assertTrue(self.contact == contact_same)

class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.address_book = AddressBook()
        self.contact1 = Contact("Martin CARPENTIER", "martin@gmail.be")
        self.contact2 = Contact("Eve SOURIS", "eve@outlook.fr")
        self.contact3 = Contact("Simon SMEESTERS", "martin@student.gouv")
        self.contact4 = Contact("Alexia BOXHO", "alexia@yahoo.ch")

    def test_add_contact(self):
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

    def test_str(self):
        self.assertEqual(str(self.address_book), "Annuaire vide")
        self.address_book.add_contact(self.contact2)
        self.assertEqual(str(self.address_book), f"Contacts dans l'annuaire:\n{self.contact2}")


    def test_get_contact_existing(self):
        self.address_book.add_contact(self.contact1)
        result = self.address_book.get_contact("Martin CARPENTIER")
        self.assertEqual(result, self.contact1)
        self.address_book.set_empty()

    def test_get_contact_nonexistent(self):
        result = self.address_book.get_contact("chat")
        self.assertIsNone(result)

    def test_remove_contact_existing(self):
        self.address_book.add_contact(self.contact1)
        self.address_book.add_contact(self.contact2)
        self.assertEqual(len(self.address_book.contacts), 2)
        self.address_book.remove_contact("Eve SOURIS")
        self.assertEqual(len(self.address_book.contacts), 1)
        self.address_book.set_empty()

    def test_remove_contact_nonexistent(self):
        self.address_book.add_contact(self.contact1)
        self.assertEqual(len(self.address_book.contacts), 1)
        self.address_book.remove_contact("chat")
        self.assertEqual(len(self.address_book.contacts), 1)
        self.address_book.set_empty()


if __name__ == "__main__":
    unittest.main()