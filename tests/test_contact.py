import unittest
from contacts.contacts_main import Contact


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_contact = Contact("test", "test", 1231231234,
                                    "test@gmail.com", "friend")

    def test_dummy_test(self):
        result = 1 + 1
        self.assertEqual(result, 2)

    def test_contact_first_name(self):
        result = self.test_contact.fname
        self.assertEqual(result, "test")

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
