#!/usr/bin/python3
"""This module contains the class HBNBCommand"""

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
from models import storage
import cmd
import shlex


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    classes = (
        "BaseModel",
        "User", "State", "City", "Amenity", "Place", "Review")
    prompt = "(hbnb) "

    def do_create(self, args):
        """Creates a new class instance"""
        args = args.split(" ")[0]
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args)()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, args):
        """Prints the representation of an instance"""
        list_args = args.split(" ")
        if not args:
            print("** class name missing **")
        elif list_args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(list_args) == 1:
            print("** instance id missing **")
        else:
            key_name = f"{list_args[0]}.{list_args[1]}"
            if key_name in storage.all():
                print(storage.all()[key_name])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance"""
        list_args = args.split(" ")
        if not args:
            print("** class name missing **")
        elif list_args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(list_args) == 1:
            print("** instance id missing **")
        else:
            key_name = f"{list_args[0]}.{list_args[1]}"
            if key_name in storage.all():
                del storage.all()[key_name]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints the representation of all instances"""
        storage_objs = storage.all()
        list_of_elements = []
        if not arg:
            list_of_elements = [str(storage_objs[el])for el in storage_objs]
            print(list_of_elements)
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage_objs.items():
                if arg == key.split(".")[0]:
                    list_of_elements.append(str(value))
            print(list_of_elements)

    def do_update(self, args):
        """Updates an instance adding or setting an attribute"""
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key_name = f"{args[0]}.{args[1]}"
            if key_name not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                if key_name in storage.all():
                    setattr(
                        storage.all()[key_name],
                        args[2], args[3])
                    storage.save()

    def emptyline(self):
        """Does nothing when a empty line is passed"""
        pass

    def do_quit(self, args):
        """Exits the programm"""
        return True

    def do_EOF(self, args):
        """Exits the programm"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
