#!/usr/bin/python3
import os
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(objects_dict, f)

    def delete(self, obj):
        """deletes obj from __objects if it’s inside"""
        check = FileStorage.__objects
        if obj in check:
            del check[obj]
        else:
            pass
        


    def reload(self):
        """deserializes the JSON file to __objects"""

        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(self.__file_path, "r") as f:
                    self.__objects = json.load(f)
                    from models.base_model import BaseModel
                    from models.user import User
                    from models.state import State
                    from models.city import City
                    from models.amenity import Amenity
                    from models.place import Place
                    from models.review import review
                    for key, val in self.__objects.items():
                        self.__objects[key] = BaseModel(**val)
            except FileNotFoundError:
                pass
