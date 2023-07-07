#!/usr/bin/python3
"""
Unittest for class Place methods
"""

import unittest
from models.place import Place


class Test_place(unittest.TestCase):
    """Test all attributes of Class place"""

    def test_name(self):
        """Checks if name is an empty string"""
        test = Place()
        self.assertEqual(type(test.name), str)
        self.assertEqual(len(test.name), 0)

    def test_city_id(self):
        """Checks if city_id is an empty string"""
        test = Place()
        self.assertEqual(type(test.city_id), str)
        self.assertEqual(len(test.city_id), 0)

    def test_user_id(self):
        """Checks if user_id is an empty string"""
        test = Place()
        self.assertEqual(type(test.user_id), str)
        self.assertEqual(len(test.user_id), 0)

    def test_description(self):
        """Checks if description is an empty string"""
        test = Place()
        self.assertEqual(type(test.description), str)
        self.assertEqual(len(test.description), 0)

    def test_number_rooms(self):
        """Checks if number rooms is an integer 0"""
        test = Place()
        self.assertEqual(type(test.number_rooms), int)
        self.assertEqual(test.number_rooms, 0)

    def test_number_bathrooms(self):
        """Checks if number bathrooms is an integer 0"""
        test = Place()
        self.assertEqual(test.number_bathrooms, 0)
        self.assertEqual(type(test.number_bathrooms), int)

    def test_max_guest(self):
        """Checks if max guest is an integer 0"""
        test = Place()
        self.assertEqual(test.max_guest, 0)
        self.assertEqual(type(test.max_guest), int)

    def test_price_by_night(self):
        """Checks if price by night is an integer 0"""
        test = Place()
        self.assertEqual(test.price_by_night, 0)
        self.assertEqual(type(test.price_by_night), int)

    def test_latitude(self):
        """Checks if latitude is a float 0.0"""
        test = Place()
        self.assertEqual(test.latitude, 0.0)
        self.assertEqual(type(test.latitude), float)

    def test_longitude(self):
        """Checks if longitude is a float 0.0"""
        test = Place()
        self.assertEqual(test.longitude, 0.0)
        self.assertEqual(type(test.longitude), float)

    def test_amenity_ids(self):
        """Checks if amenity_ids is an empty list"""
        test = Place()
        self.assertEqual(type(test.amenity_ids), list)
        self.assertEqual(len(test.amenity_ids), 0)


if __name__ == '__main__':
    unittest.main()
