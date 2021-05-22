#!/usr/bin/python3
"""class TestAmenity tester for Amenity"""
import unittest
from models.amenity import Amenity

x = Amenity()


class TestAmenity(unittest.TestCase):
    """this is to test the BaseModel"""

    def test_name(self):
        """Checks that the name is a str"""
        self.assertTrue(type(x.name) == str)


if __name__ == '__main__':
    unittest.main()