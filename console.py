#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd

import models
from models.base_model import BaseModel

# A global constant since both functions within and outside uses it.
CLASSES = [
    "BaseModel",
]


def check_args(args):
    """checks if args is valid

    Args:
        args (str): the string containing the arguments passed to a command

    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    arg_list = args.split()

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list


class HBNBCommand(cmd.Cmd):
    """The class that implements the console for the AirBnB clone web application"""
    prompt = "(hbnb) "
    storage = models.storage

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
            self.storage.save()

    def do_show(self, argv: str):
        """Prints the string representation of an instance based
        on the class name and id"""
        if (args := check_args(argv)) is not None:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = f"{args[0]}.{args[1]}"
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])

    def do_all(self, argv: str):
        """Prints all string representation of all instances based or not
        based on the class name"""
        arg_list = argv.split()
        objects = self.storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

    def do_destroy(self, argv: str):
        """Delete a class instance based on the name and given id."""
        arg_list = argv.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in CLASSES:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key in self.storage.all():
                del self.storage.all()[key]
                self.storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
