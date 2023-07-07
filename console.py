#!/usr/bin/python3
"""This module contains the class HBNBCommand"""

from models.base_model import BaseModel
import models
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

    def do_show(self, lsargs):
        """Prints the representation of an instance"""
        lsargs = lsargs.split()
        if len(lsargs) == 0:
            print("** class name missing **")
        if lsargs[0] not in HBNBCommand.acptd:
            print("** class doesn't exist **")
        if len(lsargs) == 1:
            print("** instance id missing **")
        else:
            sehobj = f"{lsargs[0]}.{lsargs[1]}"
            if sehobj in models.storage.all():
                print(models.storage.all()[sehobj])
            else:
                print("** no instance found **")

    def do_destroy(self, lsargs):
        """Deletes an instance"""
        lsargs = lsargs.split(" ")
        if len(lsargs) == 0:
            print("** class name missing **")
        if lsargs[0] in HBNBCommand.acptd:
            print("** class doesn't exist **")
        if len(lsargs) == 1:
            print("** instance id missing **")
        else:
            sehobj = f"{lsargs[0]}.{lsargs[1]}"
            if sehobj in models.storage.all():
                del models.strage.all()[sehobj]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints the representation of all instances"""
        elms = models.storage.all()
        ellist = []
        if not arg:
            ellist = [str(elms[el])for el in elms]
            print(ellist)
        elif arg not in HBNBCommand.acptd:
            print("** class doesn't exist **")
        else:
            for key, value in elms.items():
                if arg == key.split(".")[0]:
                    ellist.append(str(value))
            print(ellist)

    def update(self, lsargs):
        """Updates an instance adding or setting an attribute"""
        pass

    def emptyline(self):
        """Does nothing when a empty line is passed"""
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
