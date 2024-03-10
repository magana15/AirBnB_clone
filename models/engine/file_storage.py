#!/usr/bin/python3
"""
Module containing the FileStorage class.
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

class FileStorage:
    """
    The FileStorage class responsible for serialization and deserialization of objects.

    Attributes:
        __file_path (str): The path to the JSON file for storing serialized objects.
        __objects (dict): A dictionary to store instances using the format '<class_name>.<id>: instance'.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of stored objects.

        Returns:
            dict: A dictionary containing instances with keys in the format '<class_name>.<id>'.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj: The object to be added to the storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes and saves the objects to the JSON file.
        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def classes(self):
        """
        Returns a dictionary of available classes for serialization.

        Returns:
            dict: A dictionary containing class names as keys and corresponding class objects as values.
        """
        return {"BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

    def reload(self):
        """
        Deserializes objects from the JSON file and reloads them into the storage dictionary.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
            for key, obj_dict in data.items():
                class_name, obj_id = key.split('.')
                obj = globals()[class_name](**obj_dict)
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

