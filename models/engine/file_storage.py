#!/usr/bin/python3
"""
HBNB CLONE
"""


import json
from models.base_model import BaseModel

class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances:
    """

    def __init__(self, file_path, objects):
        self.file_path = file_path
        self.objects = {}

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        if not isinstance(value, str):
            raise TypeError("file_path must be an String")
        self.__file_path = value

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        if not isinstance(value, dict):
            raise TypeError("objects must be an dict")
        self.__objects = value

    def all(self):
        """
        public instance that returns the dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """
        public instance methods that set in
        objects the obj with key
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        public instance that serializes
        objects to the json file
        """
        fileName = self.__file_path

        with open(fileName, "w") as jsonFile:
            json.dump(self.__objects, fileName)

    def reload(self):
        """
        public instance that deserializes the json file
        """
        fileName = self.__file_path

        with open(fileName, "w") as jsonFile:
            self.__objects = json.load(fileName)
