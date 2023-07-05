#!/usr/bin/python3
"""
Base model Module
"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """Define all attributes"""

    def __init__(self):
        """Constructor method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints clase, id and dict"""
        return '[{0}] ({1}) {2}'.format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """Updates date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns object dictionary representation"""
        dict_cpy = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "update_at":
                dict_cpy[key] = value.isoformat()
            else:
                dict_cpy[key] = value
        dict_cpy["__class__"] = type(self).__name__

        return (dict_cpy)
