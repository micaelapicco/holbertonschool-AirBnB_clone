#!/usr/bin/python3
"""
Base model Module
"""

import uuid
from datetime import datetime


class BaseModel():
    """
    Defines a BaseModel
    """

    def __init__(self):
        """Constructor method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.update_at = datetime.utcnow()

    def __str__(self):
        """Prints clase, id and dict"""
        name = type(self).__name
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """Updates date"""
        self.update_at = datetime.utcnow()

    def to_dict(self):
        """Returns object dictionary representation"""
        dict_cpy = self.__dict__.copy()
        dict_cpy["__class__"] = type(self).__name__
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["update_at"] = self.update_at.isoformat()
        return (dict_cpy)

