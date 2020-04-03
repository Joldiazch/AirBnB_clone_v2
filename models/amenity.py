#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Review", backref="user", cascade="all, delete")

    amenities = relationship(
        'Amenity',
        secondary=place_amenity,
        viewonly=False,
        back_populates='place_amenities'
    )
