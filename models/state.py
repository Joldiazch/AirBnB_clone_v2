#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from models.city import City
from sqlalchemy.orm import relationship, backref
import models
import os
type_storage = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ This is the class for State
        Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if type_storage != 'db':
        @property
        def cities(self):
            """ cities for a State instance """
            all_cities = models.storage.all(City)
            return [v for v in all_cities.values() if v.state_id == self.id]
    else:
        cities = relationship(
            "City",
            backref='state',
            cascade="all, delete"
        )
