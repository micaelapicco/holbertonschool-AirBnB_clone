#!/usr/bin/python3
"""
Unittest for class City methods
"""

import unittest
from models.city import City


class Test_city(unittest.TestCase):
    """Test all attributes of Class city"""

    def test_state_id(self):
        """Checks if state id is an empty string"""
        test = City()
        self.assertEqual(type(test.state_id), str)
        self.assertEqual(len(test.state_id), 0)

    def test_name(self):
        """Checks if name is an empty string"""
        test = City()
        self.assertEqual(type(test.name), str)
        self.assertEqual(len(test.name), 0)


if __name__ == '__main__':
    unittest.main()
