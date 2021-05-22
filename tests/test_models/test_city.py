#!/usr/bin/python3
"""class TestState tester for City"""
import unittest
from models.city import City

x = City()


class TestCity(unittest.TestCase):
    """Test for BM.city.py"""

    def test_name(self):
        """Checks that the name is a str"""
        self.assertTrue(type(x.name) == str)

    def test_state_id(self):
        """Checks that the name is a str"""
        self.assertTrue(type(x.state_id) == str)


if __name__ == '__main__':
    unittest.main()