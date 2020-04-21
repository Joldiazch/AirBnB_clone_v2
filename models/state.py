#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from models.city import City
from sqlalchemy.orm import relationship, backref
import models
import os


type_storage = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref='state',
        cascade="all, delete"
    )

    @property
    def cities(self):
        """ cities for a State instance """
        if models.type_storage == 'db':
            return self.cities

        all_cities = models.storage.all(City)
        return [
            city for city in all_cities.values() if city.state_id == self.id
        ]
