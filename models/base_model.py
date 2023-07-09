#!/usr/bin/python3
"""
This modules contains the class BaseModel
"""
from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    Defines a BaseModel
    Attributes:
        id: str() of a random-generated id
        created_at: Datetime when an instance was created
        updated_at: Datetime when an instance was updated
    """

    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(
                        value,
                        "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """Prints clase, id and dict"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the date"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns the object dictionary representation"""
        dictionary = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dictionary[key] = datetime.isoformat(value)
            else:
                dictionary[key] = value
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
