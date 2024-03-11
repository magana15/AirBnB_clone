#!/usr/bin/python3
import unittest
from datetime import datetime
from models.user import User

class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def setUp(self):
        """
        Set up an instance of User for testing.
        """
        self.user = User()

    def test_user_instance_attributes(self):
        """
        Test the attributes of a User instance.
        """
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_user_id_is_string(self):
        """
        Test if the id attribute is a string.
        """
        self.assertIsInstance(self.user.id, str)

    def test_user_created_at_is_datetime(self):
        """
        Test if created_at attribute is a datetime object.
        """
        self.assertIsInstance(self.user.created_at, datetime)

    def test_user_updated_at_is_datetime(self):
        """
        Test if updated_at attribute is a datetime object.
        """
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_user_email_is_string(self):
        """
        Test if email attribute is a string.
        """
        self.assertIsInstance(self.user.email, str)

    def test_user_password_is_string(self):
        """
        Test if password attribute is a string.
        """
        self.assertIsInstance(self.user.password, str)

    def test_user_first_name_is_string(self):
        """
        Test if first_name attribute is a string.
        """
        self.assertIsInstance(self.user.first_name, str)

    def test_user_last_name_is_string(self):
        """
        Test if last_name attribute is a string.
        """
        self.assertIsInstance(self.user.last_name, str)

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.user

if __name__ == '__main__':
    unittest.main()

