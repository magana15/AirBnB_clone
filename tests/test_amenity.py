import unittest
from datetime import datetime
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class.
    """

    def setUp(self):
        """
        Set up an instance of Amenity for testing.
        """
        self.amenity = Amenity()

    def test_instance_attributes(self):
        """
        Test the attributes of an Amenity instance.
        """
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_id_is_string(self):
        """
        Test if the id attribute is a string.
        """
        self.assertIsInstance(self.amenity.id, str)

    def test_created_at_is_datetime(self):
        """
        Test if created_at attribute is a datetime object.
        """
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if updated_at attribute is a datetime object.
        """
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_name_is_string(self):
        """
        Test if the name attribute is a string.
        """
        self.assertIsInstance(self.amenity.name, str)

    def test_str_method(self):
        """
        Test the __str__ method for Amenity.
        """
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method for Amenity.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertTrue(isinstance(amenity_dict, dict))
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.amenity

if __name__ == '__main__':
    unittest.main()
