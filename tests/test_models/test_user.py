#!/usr/bin/python3
"""
Unittest for class Amenity methods
"""

import unittest
from models.user import User


class Test_user(unittest.TestCase):
    """Test of Class User"""

    def test_email(self):
        """Checks if email is an empty string"""
        test = User()
        self.assertEqual(type(test.email), str)
        self.assertEqual(len(test.email), 0)

    def test_password(self):
        """Checks if password is an empty string"""
        test = User()
        self.assertEqual(type(test.password), str)
        self.assertEqual(len(test.password), 0)

    def test_first_name(self):
        """Checks if first_name is an empty string"""
        test = User()
        self.assertEqual(type(test.first_name), str)
        self.assertEqual(len(test.first_name), 0)

    def test_last_name(self):
        """Checks if last_name  is an empty string"""
        test = User()
        self.assertEqual(type(test.last_name), str)
        self.assertEqual(len(test.last_name), 0)


if __name__ == '__main__':
    unittest.main()
