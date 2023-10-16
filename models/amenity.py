#!/usr/bin/python3
"""
Amenity Module
inherits from BaseModel class and represents an amenity in a system
it has the following attributes:
    name (str): The name of the amenity.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an amenity in a system.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
