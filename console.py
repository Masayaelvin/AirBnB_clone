#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of file - Exit the program"""
        return True
    

if __name__ == "__main__":
    HBNBCommand().cmdloop()