#!/usr/bin/python3
import cmd 
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    classes = {"BaseModel": BaseModel, "User": User, "State": State, "City": City,\
                "Amenity": Amenity, "Place": Place, "Review": Review}
    def do_create(self, arg):
        """create an instance of a class    Base = BaseModel()
        usage: create <class name>"""
        if arg == "": 
            print("** class name missing **")
        elif arg not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            for k,v in self.classes.items():
                if arg == k:
                    new_instance = v()
                    new_instance.save()
                    print(new_instance.id)
        storage.reload()
    def do_show(self, arg1):
        """show an instance of a class
        usage: show <class name> <id>"""
        args = arg1.split()
        if arg1 == "":
            print("** class name missing **")
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
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
        """print all instances of a class
        usage: all <class name>"""
        storage_check = storage.all()
        if arg == "":
            for key in storage_check:
                print(storage_check[key])
        elif arg not in self.classes.keys():
            print("** class doesn't exist **")
        else:
            if arg in self.classes.keys():
                for key in storage_check:
                    if arg in key:
                        print(storage_check[key])
    
    def do_update(self, arg):
        """update an instance of a class
        usage: update <class name> <id> <attribute name> "<attribute value>"""
        args = arg.split()
        if arg == "":
            print("** class name missing **")
        elif args[0] not in self.classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            storage_check = storage.all()
            if key in storage_check:
                setattr(storage_check[key], args[2], args[3])
                storage.save()
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn't execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
