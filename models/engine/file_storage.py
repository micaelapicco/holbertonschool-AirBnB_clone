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
        """Serializes __objects to the JSON file __file_path"""
        dic = {}
        for key, value in self.__objects.items():
            dic[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dic, self.__objects)

    def reload(self):
        """Deserializes the json file to __objects"""



#x = FileStorage()
#print(x.all())
