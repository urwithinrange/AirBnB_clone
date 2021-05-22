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
# from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import cmd
import models
dict_class = {
    "BaseModel": BaseModel()
}


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
        """string representation of an instance
        based on class name and id
        """
        a_arg = arg.split()
        if len(a_arg) < 1:
            print("** class name missing **")
            return
        if len(a_arg) < 2:
            print("** instance id missing **")
            return
        if a_arg[0] not in dict_class:
            print("** class doesn't exist **")
            return
        try:
            video = a_arg[0] + "." + a_arg[1]
            print(models.storage.all()[video])
        except:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Be kind, do the video thing"""
        a_arg = arg.split()
        rew = a_arg[0]
        ind = a_arg[1]


        if len(a_arg) < 1:
            print("** class name missing **")
            return
        if len(a_arg) < 2:
            print("** instance id missing **")
            return
        if a_arg[0] not in dict_class:
            print("** class doesn't exist **")
            return
        try:
            rewind = rew + "." + ind
            if rewind in models.storage.all():
                models.storage.all().pop(rewind)

        except:
            print("** no instance found **")

    def do_all(self, arg=None):
        """Print list of strings of all instances based in the class"""
        dcbrilliance = []
        if not arg:
            for iteration in models.storage.all():
                dcbrilliance.append(str(models.storage.all()[iteration]))
            print(dcbrilliance)
            return
        try:
            if arg:
                tmp_dict = models.storage.all()
                for ite in tmp_dict.keys():
                    print(ite)
                    a_obj = tmp_dict[ite]
                    dcbrilliance.append(str(a_obj))
                print(dcbrilliance)

        except:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()