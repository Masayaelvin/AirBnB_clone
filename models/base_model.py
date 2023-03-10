#!/usr/bin/env python3
import uuid 
from datetime import datetime

class BaseModel:
    """Base model for all other classes. it contains
    attributes and methods for the instances of the base model."""

    def __init__(self, *args, **kwargs):
        """we are initalising public instances"""
        if not kwargs:
            self.id =  str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key and value != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """returning te string representation of the BaseModel"""
        return "[{}] ({}) {}".format(type(self).__name__,self.id,self.__dict__)

    def save(self):
        """updates the public instance attribut updated_at with the currebnt date and
        time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary repredentation of the Base Model"""

        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] =self.created_at.isoformat()
        dict_copy['updated_at'] =self.updated_at.isoformat()
        dict_copy['created_at'] = type(self).__name__
        return dict_copy
