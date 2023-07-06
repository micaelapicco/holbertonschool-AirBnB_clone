#!/usr/bin/python3
"""This module contains the class HBNBCommand"""

from models.base_model import BaseModel
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    acptd = ("BaseModel", )
    prompt = "(hbnb) "

    def do_create(self, inptcls):
        """Creates a new class isntance"""
        if not inptcls:
            print("** class name missing **")

        if " " in inptcls:
            inptcls = inptcls.split(" ")[0]
        if inptcls not in HBNBCommand.acptd:
            print("** class doesn't exist **")
        else:
            nince = eval(inptcls)()
            print(nince.id)
            nince.save()

    def emptyline(self):
        """Takes action when an passed empty line as input"""
        pass

    def do_quit(self, input):
        """Exits the programm"""
        return True

    def do_EOF(self, input):
        """Exits the programm"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
