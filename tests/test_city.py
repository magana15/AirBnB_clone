#!/usr/bin/python3
import unittest
from datetime import datetime
from models.city import City

class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """
        Set up an instance of City for testing.
        """
        self.city = City()

    def test_city_instance_attributes(self):
        """
        Test the attributes of a City instance.
        """
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_city_id_is_string(self):
        """
        Test if the id attribute is a string.
        """
        self.assertIsInstance(self.city.id, str)

    def test_city_created_at_is_datetime(self):
        """
        Test if created_at attribute is a datetime object.
        """
        self.assertIsInstance(self.city.created_at, datetime)

    def test_city_updated_at_is_datetime(self):
        """
        Test if updated_at attribute is a datetime object.
        """
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_city_state_id_is_string(self):
        """
        Test if state_id attribute is a string.
        """
        self.assertIsInstance(self.city.state_id, str)

    def test_city_name_is_string(self):
        """
        Test if name attribute is a string.
        """
        self.assertIsInstance(self.city.name, str)

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.city

if __name__ == '__main__':
    unittest.main()

