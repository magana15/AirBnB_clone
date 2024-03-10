#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def __init__(self):
        """Initialize the HBNBCommand instance."""
        super().__init__()
        self.file_storage = FileStorage()
        self.file_storage.reload()

    def do_quit(self, arg):
        """Exit the command interpreter."""
        print("Quitting...")
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter (EOF)."""
        print("Exiting...")
        return True

    def emptyline(self):
        """Do nothing on empty line + ENTER."""
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel.

        Usage: create <class_name>

        Args:
            arg (str): The class name for which a new instance should be created.

        Notes:
            If the class name is missing, print "** class name missing **".
            If the class name doesn’t exist, print "** class doesn't exist **".
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name = arg
            new_instance = eval(class_name)()
            self.file_storage.new(new_instance)
            self.file_storage.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show the string representation of an instance.

        Usage: show <class_name> <id>

        Args:
            arg (str): The command arguments, including class name and instance id.

        Notes:
            If the class name is missing, print "** class name missing **".
            If the class name doesn’t exist, print "** class doesn't exist **".
            If the id is missing, print "** instance id missing **".
            If the instance of the class name doesn’t exist for the id, print "** no instance found **".
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            class_name = args[0]
            obj_id = args[1]

            if class_name not in globals():
                print("** class doesn't exist **")
                return

            key = "{}.{}".format(class_name, obj_id)
            all_objects = self.file_storage.all()

            if key not in all_objects:
                print("** no instance found **")
                return

            print(all_objects[key])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.

        Usage: destroy <class_name> <id>

        Args:
            arg (str): The command arguments, including class name and instance id.

        Notes:
            If the class name is missing, print "** class name missing **".
            If the class name doesn’t exist, print "** class doesn't exist **".
            If the id is missing, print "** instance id missing **".
            If the instance of the class name doesn’t exist for the id, print "** no instance found **".
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            class_name = args[0]
            obj_id = args[1]

            if class_name not in globals():
                print("** class doesn't exist **")
                return

            key = "{}.{}".format(class_name, obj_id)
            all_objects = self.file_storage.all()

            if key not in all_objects:
                print("** no instance found **")
                return

            del all_objects[key]
            self.file_storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances.

        Usage: all [class_name]

        Args:
            arg (str): The class name (optional).

        Notes:
            The printed result must be a list of strings.
            If the class name doesn’t exist, print "** class doesn't exist **".
        """
        try:
            if not arg:
                objs = self.file_storage.all().values()
            else:
                class_name = arg
                if class_name not in globals():
                    print("** class doesn't exist **")
                    return
                objs = [obj for key, obj in self.file_storage.all().items() if class_name in key]

            print([str(obj) for obj in objs])
        except Exception as e:
            print(e)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id.

        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"

        Args:
            arg (str): The command arguments, including class name, instance id, attribute name, and attribute value.

        Notes:
            If the class name is missing, print "** class name missing **".
            If the class name doesn’t exist, print "** class doesn't exist **".
            If the id is missing, print "** instance id missing **".
            If the instance of the class name doesn’t exist for the id, print "** no instance found **".
            If the attribute name is missing, print "** attribute name missing **".
            If the value for the attribute name doesn’t exist, print "** value missing **".
            Only one attribute can be updated at a time.
            You can assume the attribute name is valid (exists for this model).
            The attribute value must be casted to the attribute type.
            Only “simple” arguments can be updated: string, integer, and float.
            You can assume nobody will try to update lists of ids or datetime.
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            class_name = args[0]
            obj_id = args[1]

            if class_name not in globals():
                print("** class doesn't exist **")
                return

            key = "{}.{}".format(class_name, obj_id)
            all_objects = self.file_storage.all()

            if key not in all_objects:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return

            attribute_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return

            attribute_value = args[3]
            setattr(all_objects[key], attribute_name, attribute_value)
            self.file_storage.save()
        except IndexError:
            print("** instance id missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

