#!/usr/bin/python3
"""
Unittest for class BaseModel methods
"""

import unittest
from models.base_model import BaseModel


class Test_amenity(unittest.TestCase):
    """Test of Class BaseModel"""

    def test_str(self):
        """Checks if name is an empty string"""
        test = BaseModel()


if __name__ == '__main__':
    unittest.main()
