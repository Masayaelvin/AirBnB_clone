#!/usr/bin/python3
import json
import os


class FileStorage:
    """
    Class for storing the files
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Displays all objects in the dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as f:
            json.dump(objects_dict, f, indent=4)

    def delete(self, arg):
        """
        deletes obj from __objects if it’s inside
        """
        if arg in FileStorage.__objects:
            del FileStorage.__objects[arg]
            self.save()

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.isfile(FileStorage.__file_path) \
                and os.path.getsize(FileStorage.__file_path) > 0:
            try:
                with open(self.__file_path, "r") as f:
                    self.__objects = json.load(f)
                    from models.base_model import BaseModel
                    from models.user import User
                    from models.state import State
                    from models.city import City
                    from models.amenity import Amenity
                    from models.place import Place
                    from models.review import Review
                    classes = {
                            "BaseModel": BaseModel,
                            "User": User,
                            "State": State,
                            "City": City,
                            "Amenity": Amenity
                            "Place": Place,
                            "Review": Review
                            }
                    for key, val in self.__objects.items():
                        cls_name = val["__class__"]
                        cls_name = classes[cls_name]
                        self.__objects[key] = cls_name(**val)
                except FileNotFoundError:
                    pass
