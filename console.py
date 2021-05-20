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

# import models
# import sys
import cmd
# from models.engine.file_storage import file_storage
# from models.base_model import BaseModel


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()