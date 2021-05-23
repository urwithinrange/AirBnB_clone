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
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import cmd
import models
dict_class = {
    'BaseModel': BaseModel,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review,
    'State': State,
    'User': User
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
            return

        for key, value in dict_class.items():
            if arg == key:
                a_value = value()
                print(a_value.id)
                a_value.save()
                break
        else:
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

        if len(a_arg) < 1:
            print("** class name missing **")
            return
        if a_arg[0] not in dict_class:
            print("** class doesn't exist **")
            return
        if len(a_arg) < 2:
            print("** instance id missing **")
            return
        rew = a_arg[0]
        ind = a_arg[1]
        rewind = rew + "." + ind
        if rewind in models.storage.all():
                models.storage.all().pop(rewind)
                models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print list of strings of all instances based in the class"""
        dc = []
        if not arg:
            for iteration in models.storage.all():
                dc.append(str(models.storage.all()[iteration]))
            return
        if arg in dict_class:
           tmp_dict = models.storage.all()
            for ite in tmp_dict.keys():
                if arg == ite.split(".")[0]:
                    a_obj = tmp_dict[ite]
                    dc.append(str(a_obj))
            print(dc)
        else:
            print("** class doesn't exist **")
            
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
