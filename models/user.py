#!/usr/bin/python3
"""Contains the class user"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines an User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
