#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from os import getenv
import models


type_storage = getenv('HBNB_TYPE_STORAGE')


class Place(BaseModel, Base):
    """This is the class for Place
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)

    latitude = Column(Float)
    longitude = Column(Float)

    amenity_ids = []

    metadata = Base.metadata

    place_amenity = Table(
        'place_amenity',
        metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False
        ),
        Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False
        )
    )

    if type_storage == 'db':
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete"
        )

        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False,
            back_populates='place_amenities'
        )

    else:
        @property
        def reviews(self):
            """Getter"""
            return self.reviews

        @property
        def amenities(self):
            """Getter"""
            data = models.storage.all(models.amenity.Amenity)
            return [obj for obj in data if obj.place_id == self.id]

        @amenities.setter
        def amenities(self, obj=None):
            """ setter method """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.amenities.id)
