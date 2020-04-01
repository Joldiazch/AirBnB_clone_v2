#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from models import storage
from models.city import City


class State(BaseModel):
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
        all_cities = storage.all(City)
        return [city for city in all_cities if city['state_id'] == self.id]
