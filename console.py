#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd

import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review

# A global constant since both functions within and outside uses it.
CLASSES = [
    "BaseModel",
    "User",
    "City",
    "Place",
    "State",
    "Amenity",
    "Review"
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
    """The class that implements the console
    for the AirBnB clone web application
    """
    prompt = "(hbnb) "
    storage = models.storage

    def emptyline(self):
        """Command to executed when empty line + <ENTER> key"""
        pass

    def do_EOF(self):
        """Command to be executed when Ctrl-c (EOF) is entered"""
        print("")
        return True

    def do_quit(self, argv):
        """When executed, exits the console."""
        return True

    def do_create(self, argv):
        """Creates a new instance of BaseModel, saves it (to a JSON file)
        and prints the id"""
        if (args := check_args(argv)) is not None:
            print(eval(args[0])().id)
            self.storage.save()

    def do_show(self, argv):
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

    def do_all(self, argv):
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

    def do_destroy(self, argv):
        """Delete a class instance based on the name and given id."""
        if (arg_list := check_args(argv)) is not None:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*arg_list)
                if key in self.storage.all():
                    del self.storage.all()[key]
                    self.storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, argv):
        """Updates an instance based on the class name and id by adding or
        updating attribute and save it to the JSON file."""
        if (arg_list := check_args(argv)) is not None:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in self.storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(obj, arg_list[2], arg_list[3])
            self.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
