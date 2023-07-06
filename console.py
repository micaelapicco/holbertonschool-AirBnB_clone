#!/usr/bin/python3
"""This module contains the class HBNBCommand"""

from models.base_model import BaseModel
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_create(self, input_cls):
        """Creates a new class"""
        if not input_cls:
            print(**class doesn´t missing**)

        split()
        eval(input_cls)()

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
