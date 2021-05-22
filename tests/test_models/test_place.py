#!/usr/bin/python3
"""class TestState tester for Place"""
import unittest
from models.place import Place

x = Place()


class TestPlace(unittest.TestCase):
    """Test for BM.place.py"""

    def test_user_id(self):
        """Checks that the user_id is a str"""
        self.assertTrue(type(x.user_id) == str)

    def test_city_id(self):
        """Checks that the city_id is a str"""
        self.assertTrue(type(x.city_id) == str)

    def test_name(self):
        """Checks that the name is a str"""
        self.assertTrue(type(x.name) == str)

    def test_description(self):
        """Checks that the description is a str"""
        self.assertTrue(type(x.description) == str)

    def test_number_rooms(self):
        """Checks that the number of rooms is a int"""
        self.assertTrue(type(x.number_rooms) == int)

    def test_number_bathrooms(self):
        """Checks that the city_id is a int"""
        self.assertTrue(type(x.number_bathrooms) == int)

    def test_max_guests(self):
        """Checks that the max guests is a int"""
        self.assertTrue(type(x.max_guest) == int)

    def test_price_by_night(self):
        """Checks that the price by night is a int"""
        self.assertTrue(type(x.price_by_night) == int)

    def test_latitude(self):
        """Checks that the latitude is a float"""
        self.assertTrue(type(x.latitude) == float)

    def test_longitude(self):
        """Checks that the longitude is a float"""
        self.assertTrue(type(x.longitude) == float)

    def test_amenity_ids(self):
        """Checks that the amenity ids is a list"""
        self.assertTrue(type(x.amenity_ids) == list)


if __name__ == '__main__':
    unittest.main()