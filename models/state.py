#!/usr/bin/python3
"""
State Class from Models Module
"""
from sqlalchemy import Column, String
from sqlalchemy import *
from sqlalchemy.orm import *
from models.base_model import BaseModel, Base
from os import getenv, environ


class State(BaseModel, Base):
    """State class handles all application states"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade="all")
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)

    if environ.get("HBNB_TYPE_STORAGE") is None or \
       getenv("HBNB_TYPE_STORAGE") != 'db':
        def cities(self):
            from models import storage
            cities_dict = storage.all("City")
            cities = []
            for item in cities_dict.values():
                if item['state_id'] == self.id:
                    cities.append(item)
            return cities
