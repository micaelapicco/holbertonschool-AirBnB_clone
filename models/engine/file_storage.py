#!/usr/bin/python3
"""Contains the class FileStorage"""

from os import path
import json


class FileStorage:
    """Handles json serialization and deserialization"""

    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """Returns __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects, obj"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path"""
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def reload(self):
        """Deserializes the json file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    self.new(eval(value["__class__"])(**value))
