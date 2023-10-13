#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_create(self, arg):
        """create an instance of a class    Base = BaseModel()
        usage: create <class name>"""
        if arg == "":
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            Base = BaseModel()
            print(Base.id)
            Base.save()
    
    def do_show(self, arg1):
        """show the string representation of an instance based on the class name and id
        usage: show <class name> <id>"""
        args = arg1.split()
        if arg1 == "":
            print("** class name missing **")
        elif args[0] != "BaseModel":
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

    def do_destroy(self, arg1): ##doesn't update the json file
        '''Deletes an instance based on the class name and id (save the change into the JSON file)
        usage: destroy <class name> <id>'''
        args = arg1.split()
        if arg1 == "":
            print("** class name missing **")
        elif args[0] != "BaseModel":
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
        elif args[0] != "BaseModel":
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
        elif args[0] != "BaseModel":
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