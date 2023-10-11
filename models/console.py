import cmd

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        print()
        return True

    def emptyline(self):
        pass

    # def prompt(self):
    #     pass

    def do_help(self, arg):
        cmd.Cmd.do_help(self, arg)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
