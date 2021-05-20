#!/usr/bin/python3
"""
Write a class FileStorage that serializes instances
to a JSON file and deserializes JSON file to instances:
-
Private class attributes:
__file_path: string - path to the JSON file (ex: file.json)
__objects: dictionary - empty but will store all objects
by <class name>.id (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
-
Public instance methods:
all(self): returns the dictionary __objects
new(self, obj): sets in __objects the obj with key <obj class name>.id
save(self): serializes __objects to the JSON file (path: __file_path)
reload(self): deserializes the JSON file to __objects
(only if the JSON file (__file_path) exists ; otherwise, do nothing. If
the file doesn’t exist, no exception should be raised)
--
Update models/__init__.py: to create a unique FileStorage instance for your application
-
import file_storage.py
create the variable storage, an instance of FileStorage
call reload() method on this variable
Update models/base_model.py: to link your BaseModel to FileStorage by using the variable storage
-
import the variable storage
in the method save(self):
call save(self) method of storage
__init__(self, *args, **kwargs):
if it’s a new instance (not from a dictionary representation), add a call to the method new(self) on storage
"""
import json
from models import BaseModel


class FileStorage:
    """Stores files to recover from JSON strings"""

    __file_path = "file.json"
    __objects = dict()

    def __init__(self):
        """Welp"""
        pass

    def all(self):
        """returns dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets obj as a new key in FS.__objects()"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name_, obj.id)] = id

    def save(self):
        """serializes obj to JSON"""
        """woof as empty dict, womp as iterable"""
        """x as iterable, y as value of iterable loc"""
        woof = {}
        with open(FileStorage.__file_path, "w",  encoding="UTF8") as womp:
            for x, y in FileStorage.__objects.items():
                woof[x] = y.to_dict()
        json.dump(woof, womp)

    def reload(self):
        """deserializes JSON to obj"""
        try:
            with open(FileStorage.__file_path, "r", emcoding="UTF8") as womp:
              woof = json.load(womp)
            for x, y in woof.items():
                FileStorage.__objects[x] = BaseModel(**y)
        except:
            pass
