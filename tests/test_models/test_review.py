#!/usr/bin/python3
"""
Unittest for class Review methods
"""

import unittest
from models.review import Review


class Test_review(unittest.TestCase):
    """Test all attributes of Review place"""

    def test_place_id(self):
        """checks if place id is an empty string"""
        test = Review()
        self.assertEqual(type(test.place_id), str)
        self.assertEqual(len(test.place_id), 0)

    def test_user_id(self):
        """checks if user_id is an empty string"""
        test = Review()
        self.assertEqual(type(test.user_id), str)
        self.assertEqual(len(test.user_id), 0)

    def test_text(self):
        """checks if text is an empty string"""
        test = Review()
        self.assertEqual(type(test.text), str)
        self.assertEqual(len(test.text), 0)

if __name__ == '__main__':
    unittest.main()