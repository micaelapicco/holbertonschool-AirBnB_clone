#!/usr/bin/python3
"""
Unittest for class Amenity methods
"""

import unittest
from models.amenity import Amenity


class Test_amenity(unittest.TestCase):
    """Test of Class Amenity"""

    def test_name(self):
        """Checks if name is an empty string"""
        test = Amenity()
        self.assertEqual(type(test.name), str)
        self.assertEqual(len(test.name), 0)


if __name__ == '__main__':
    unittest.main()
