#!/usr/bin/python3
"""
Write a program called console.py that contains
the entry point of the command interpreter:
-
You must use the module cmd
Your class definition must be:
class HBNBCommand(cmd.Cmd):
_
Your command interpreter should implement:
quit and EOF to exit the program
help (this action is provided by default by cmd but you
should keep it updated and documented as you work through tasks)
a custom prompt: (hbnb)
-
an empty line + ENTER shouldn’t execute anything
Your code should not be executed when imported
"""

# import sys
# from models.engine.file_storage import file_storage
import models.engine.file_storage
from models.base_model import BaseModel
import cmd
import models
dict_class = {"BaseModel": BaseModel()}


class HBNBCommand(cmd.Cmd):
    """The CLI for our instances"""

    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """If we want to exit, do this"""
        return True

    def do_quit(self, arg):
        """Naw, I aint no quitter"""
        return True

    def emptyline(self):
        """We want an empty line to do nothing"""
        pass

    def do_create(self, arg):
        """creates a class instance"""
        if not arg:
            print("** class name missing **")
            return False
        try:
            for key, value in dict_class.items():
                if arg == key:
                    a_value = value
                    print(a_value.id)
                    a_value.save()
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        a_arg = arg.split()

        vid = a_arg[0]
        eo = a_arg[1]
        video = vid + "." + eo

        print(eo)
        print(vid)
        print(models.storage.all()[video])

if __name__ == '__main__':
    HBNBCommand().cmdloop()