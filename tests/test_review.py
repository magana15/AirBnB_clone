#!/usr/bin/python3
import unittest
from datetime import datetime
from models.review import Review

class TestReview(unittest.TestCase):
    """
    Test cases for Review class.
    """

    def setUp(self):
        """
        Set up an instance of Review for testing.
        """
        self.review = Review()

    def test_review_instance_attributes(self):
        """
        Test the attributes of a Review instance.
        """
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_review_id_is_string(self):
        """
        Test if the id attribute is a string.
        """
        self.assertIsInstance(self.review.id, str)

    def test_review_created_at_is_datetime(self):
        """
        Test if created_at attribute is a datetime object.
        """
        self.assertIsInstance(self.review.created_at, datetime)

    def test_review_updated_at_is_datetime(self):
        """
        Test if updated_at attribute is a datetime object.
        """
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_review_place_id_is_string(self):
        """
        Test if place_id attribute is a string.
        """
        self.assertIsInstance(self.review.place_id, str)

    def test_review_user_id_is_string(self):
        """
        Test if user_id attribute is a string.
        """
        self.assertIsInstance(self.review.user_id, str)

    def test_review_text_is_string(self):
        """
        Test if text attribute is a string.
        """
        self.assertIsInstance(self.review.text, str)

    # Add more test cases as needed...

    def tearDown(self):
        """
        Clean up after each test.
        """
        del self.review

if __name__ == '__main__':
    unittest.main()

