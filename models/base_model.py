#!/usr/bin/python3
import datetime
import uuid
from models import storage

class BaseModel:
        
    #id = uuid.uuid4()
    #created_at = datetime.datetime.now()
    #updated_at = datetime.datetime.now()

    def __init__(self, *args, **kwargs):
        #if kwargs is npot empty
        id = str(uuid.uuid4())
        created_at = datetime.datetime.now()
        updated_at = datetime.datetime.now()
        if kwargs and kwargs != None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
                storage.new(self)

        #otherwise
        if "id" not in kwargs.keys():
            self.id = str(uuid.uuid4())
        if "created_at" not in kwargs.keys():
            self.created_at = datetime.datetime.now()
        if "updated_at" not in kwargs.keys():
            self.updated_at = datetime.datetime.now()
        storage.new(self)


    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
    
    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()
    
    def delete(self):
        key = self.__class__.__name__ + "." + self.id
        storage.delete(key)
    
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return(obj_dict)
