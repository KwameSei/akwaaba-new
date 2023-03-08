#!/usr/bin/env python3
"""A module to implement the BaseModel class"""

from datetime import datetime
import sqlalchemy
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from uuid import uuid4
#from models import storage_type

Base = declarative_base()


class BaseModel:
    """BaseModel defines all common attributes
    or methods for other classes"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initializing class attributes"""

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

            if storage_type == "db":
                if not hasattr(kwargs, 'id'):
                    setattr(self, 'id', str(uuid4()))
                if not hasattr(kwargs, 'created_at'):
                    setattr(self, 'created_at', datetime.now())
                if not hasattr(kwargs, 'updated_at'):
                    setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """print format of the output"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        from models import storage
        self.updated_at = datetime.today()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance:
        - only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
                new_dict[key] = value
        return new_dict

    def delete(self):
        """Deleting current instance from stoarage"""
        from models import storage
        storage.delete(self)
