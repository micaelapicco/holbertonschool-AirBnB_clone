#!/usr/bin/python3
"""Contains the class FileStorage"""

from os import path


class FileStorage:
    """Handles json serialization and deserialization"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects, obj"""
        self.__objects[str(type(name)) + "." + obj.id]

    def save(self):
        """Serializes _objets to the JSON file __file_path"""
        with open(__file_path, "w", encoding="utf-8") as f:
            f.dump(self.__objects, f)


#x = FileStorage()
#print(x.all())
