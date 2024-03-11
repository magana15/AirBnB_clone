import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def setUp(self):
        """
        Set up an instance of BaseModel for testing.
        """
        self.base_model = BaseModel()

    def test_instance_attributes(self):
        """
        Test the attributes of a BaseModel instance.
        """
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))

    def test_id_is_string(self):
        """
        Test if the id attribute is a string.
        """
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        """
        Test if created_at attribute is a datetime object.
        """
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test if updated_at attribute is a datetime object.
        """
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_method(self):
        """
        Test the __str__ method for BaseModel.
        """
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method for BaseModel.
        """
        model_dict = self.base_model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.base_model.id)

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.base_model

if __name__ == '__main__':
    unittest.main()
