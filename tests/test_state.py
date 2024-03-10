#!/usr/bin/python3
import unittest
from datetime import datetime
from models.state import State

class TestState(unittest.TestCase):
    """
    Test cases for State class.
    """

    def setUp(self):
        """
        Set up an instance of State for testing.
        """
        self.state = State()

    def test_state_instance_attributes(self):
        """
        Test the attributes of a State instance.
        """
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))

    def test_state_id_is_string(self):
        """
        Test if the id attribute is a string.
        """
        self.assertIsInstance(self.state.id, str)

    def test_state_created_at_is_datetime(self):
        """
        Test if created_at attribute is a datetime object.
        """
        self.assertIsInstance(self.state.created_at, datetime)

    def test_state_updated_at_is_datetime(self):
        """
        Test if updated_at attribute is a datetime object.
        """
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_state_name_is_string(self):
        """
        Test if name attribute is a string.
        """
        self.assertIsInstance(self.state.name, str)

    # Add more test cases as needed...

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.state

if __name__ == '__main__':
    unittest.main()

