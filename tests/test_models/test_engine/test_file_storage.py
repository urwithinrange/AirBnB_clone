#!/usr/bin/python3
"""Class TestFileStorage"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

var = FileStorage()
base = BaseModel()


class TestFileStorage(unittest.TestCase):
    """This class tests the file_storage methods"""

    def test_filepath(self):
        """tests that file_path contains a string"""
        var.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_object(self):
        """test that the  object is a dictionary"""
        self.assertTrue(type(var.all()) is dict)

    def test_all(self):
        pass

    def test_new(self):
        """testing the new module"""
        tmp_dict = var.all().copy()  # Create a tmp to test if new works
        BaseModel()  # create new id and FS will update __obj dict
        self.assertFalse(var.all() == tmp_dict)  #

    def test_save(self):
        """tests that save creates a string"""
        try:
            os.remove("file.json")
        except:
            pass
        tmp = base.save()
        self.assertFalse(tmp == "file.json")

    def test_reload(self):
        """test the reload module"""
        var.save()
        var.reload()
        tmp1 = var.all()
        var.save()
        var.reload()
        tmp2 = var.all()
        self.assertEqual(tmp2, tmp1)

    def test_

if __name__ == '__main__':
    unittest.main()
