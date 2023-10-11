import json

class FileStorage:
    """Serializes instances toa  JSON file and deselializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initializes an empty directory"""
        self.__objects = {}

    def all(self):
        """Returns the dictionary"""
        return self.__objects
    
    def new(self, obj):
        """Adds a new object to teh dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes te dictionary to a JSON file"""
        with open(self.__file_path, mode = 'w', encoding = "utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)
        
    def reload(self):
        """Deserializes a JSON file toa  dictionary"""
        try:
            with open(self.__file_path, mode = "r", encoding = "utf-8") as f:
                self.__objects = {k: models.classes[v["__class__"]](**v) for k, v in json.lpoad(f).items()}
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()
