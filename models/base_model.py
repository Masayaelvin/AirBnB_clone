#!/usr/bin/python3
import datetime
import uuid
from models import storage


class BaseModel:
    """
    BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        Object innit
        """
        if kwargs and kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.\
                        strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

        if "id" not in kwargs.keys():
            self.id = str(uuid.uuid4())
        if "created_at" not in kwargs.keys():
            self.created_at = datetime.datetime.now()
        if "updated_at" not in kwargs.keys():
            self.updated_at = datetime.datetime.now()
        storage.new(self)

    def __str__(self):
        """
        String representation of object
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        Oject save function
        """
        storage.save()
        self.updated_at = datetime.datetime.now()

    def delete(self):
        """
        Object delete function
        """
        storage.delete(self)

    def to_dict(self):
        """
        Object dictionary representation
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return (obj_dict)
