#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"    
    classes = {"BaseModel":BaseModel, "User":User, "State":State, "City":City, "Amenity":Amenity, \
                               "Place": Place, "review":review}
    def do_create(self, arg):
        """create an instance of a class    Base = BaseModel()
        usage: create <class name>"""
        if arg == "":
            print("** class name missing **")
        elif arg not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            for k,v in self.classes.items():
                if k == arg:
                    instance = v()
                    print(instance.id)
                    instance.save()
            storage.reload()
                
    
    def do_show(self, arg1):
        """show the string representation of an instance based on the class name and id
        usage: show <class name> <id>"""
        args = arg1.split()
        if arg1 == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            storage_check = storage.all()
            if key in storage_check:
                print(storage_check[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg1): 
        '''Deletes an instance based on the class name and id (save the change into the JSON file)
        usage: destroy <class name> <id>'''
        args = arg1.split()
        if arg1 == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            storage_check = storage.all()
            if key in storage_check:
                storage.delete(storage_check[key])    
                storage.delete(key)
                storage.save()
                storage.reload()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name
        usage: all <class name>"""
        args = arg.split()
        storage_check = storage.all()
        if arg == "":
            for key in storage_check:
                print(storage_check[key])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key in storage_check:
                if args[0] in key:
                    print(storage_check[key])
    
    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
        usage: update <class name> <id> <attribute name> "<attribute value>"""
        args = arg.split()
        storage_check = storage.all()
        if arg == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage_check:
                setattr(storage_check[key], args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")
           

        
    def do_quit(self, arg):
        """command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of file - Exit the program"""
        return True
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()