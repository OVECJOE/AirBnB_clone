#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd

import models
from models.base_model import BaseModel


def check_args(args):
    """checks if args is valid

    Args:
        args (str): the string containing the arguments passed to a command

    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    __classes = [
        "BaseModel",
    ]

    arg_list = args.split()

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in __classes:
        print("** class doesn't exist **")
    else:
        return arg_list


class HBNBCommand(cmd.Cmd):
    """The class that implements the console for the AirBnB clone web application"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Command to executed when empty line + <ENTER> key"""
        pass

    def do_EOF(self):
        """Command to be executed when Ctrl-c (EOF) is entered"""
        print("")
        return True

    def do_quit(self, status: int):
        """When executed, exits the console."""
        return True

    def do_create(self, argv: str):
        """Creates a new instance of BaseModel, saves it (to a JSON file)
        and prints the id"""
        if (args := check_args(argv)) is not None:
            print(eval(args[0])().id)
            models.storage.save()

    def do_show(self, argv: str):
        """Prints the string representation of an instance based
        on the class name and id"""
        if (args := check_args(argv)) is not None:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in models.storage.all():
                    print("** no instance found **")
                else:
                    print(models.storage.all()[key])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
