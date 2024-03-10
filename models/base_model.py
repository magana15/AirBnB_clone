#!/usr/bin/python3
"""
Module containing the BaseModel class.
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    The BaseModel class representing the base model for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list (not used).
            **kwargs: Key-value pairs of attributes for initialization.
                      If provided, it populates the instance attributes accordingly.
                      If not provided, it generates a new id and sets created_at and updated_at.

        Attributes:
            id (str): Unique identifier for the instance.
            created_at (datetime): Date and time of instance creation.
            updated_at (datetime): Date and time of the last instance update.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation in the format: "[<class name>] (<id>) <__dict__>"
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Saves the current instance to the storage and updates the storage file.
        """
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary containing all keys/values of __dict__ of the instance.
                  Includes '__class__', 'created_at', and 'updated_at'.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

