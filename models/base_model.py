#!/usr/bin/python3
'''
Defines BaseModel as the superclass for all other classes in the AirBnB Project.
'''
import uuid
from datetime import datetime
from . import storage


class BaseModel:
    '''
    BaseModel provides methods and attributes for subclasses in the AirBnb project.

    Attributes:
        id (str): A unique identifier for each instance, assigned using uuid4().
        created_at (datetime): A Datetime object assigned to BaseModels
            when instances are created.
        updated_at (datetime): A datetime object assigned to each instance
            of BaseModel at initialization, and reset when save() is called.
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initialization method called each time an instance is created.

        Args:
            *args: Variable length argument list (unused in this implementation).
            **kwargs: Arbitrary keyword arguments. Expected keys: id, created_at, updated_at.
        '''
        if kwargs:
            self.load_from_kwargs(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def load_from_kwargs(self, kwargs):
        '''
        Load instance attributes from kwargs.

        Args:
            kwargs (dict): Key-value pairs to initialize the instance.
        '''
        for key, value in kwargs.items():
            if key != "__class__":
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)

    def __str__(self):
        '''
        Set the string representation of the BaseModel object.

        Returns:
            str: String representation in the format "[<class name>] (<self.id>) <self.__dict__>"
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Update the public attribute `updated_at` with the current time and save the changes.
        '''
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        Serialize the object by returning a dictionary representation.

        Returns:
            dict: A dictionary containing keys/values of the instance with additional "__class__" key.
        '''
        result = self.__dict__.copy()
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        result['__class__'] = self.__class__.__name__
        return result

