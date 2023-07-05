#!/usr/bin/python3
"""
This modules contains the class BaseModel
"""

import uuid
from datetime import datetime


class BaseModel():
    """
    Defines a BaseModel
    Attributes:
        id: str() of a random-generated id
        created_at: Datetime when an instance was created
        updated_at: Datetime when an instance was updated
    """

    def __init__(self):
        """Constructor method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints clase, id and dict"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns object dictionary representation"""
        dict_cpy = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dict_cpy[key] = datetime.isoformat(value)
            else:
                dict_cpy[key] = value
        dict_cpy["__class__"] = self.__class__.__name__

        return (dict_cpy)
