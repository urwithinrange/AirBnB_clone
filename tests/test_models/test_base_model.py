#!/usr/bin/python3
"""class TestBaseModel tester for base model"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import unittest
import os

var = BaseModel()
varf = FileStorage()


class TestBaseModel(unittest.TestCase):
    """this is to test the BaseModel"""

    def test_str(self):
        """Testing the __str__ method"""
        self.assertEqual(str(var), "[{}] ({}) {}".format(
                         var.__class__.__name__, var.id, var.__dict__))

    def test_to_dict(self):
        """test that the function works"""
        a_dict = var.to_dict()
        self.assertIsInstance(a_dict["created_at"], str)

    def test_save(self):
        """method to test save"""
        a_dict = var.to_dict()
        var.save()
        attr1 = var.updated_at
        var.save()
        attr2 = var.updated_at
        self.assertFalse(attr1 == attr2)
        self.assertEqual(a_dict["__class__"], "BaseModel")

    def test_id(self):
        """Testing that id is a string"""
        self.assertTrue(type(var.id) is str)

    def test_created(self):
        """Verifying """
        self.assertTrue(type(var.created_at) is datetime)

    # def test__init__(self):


if __name__ == '__main__':
    unittest.main()