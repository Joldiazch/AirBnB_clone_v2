#!usr/bin/python3
""" DataBase storage """
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.user import User
from models.base_model import BaseModel, Base
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os


""" load env variables """
dev = os.getenv('HBNB_ENV')
username = os.getenv('HBNB_MYSQL_USER')
passw = os.getenv('HBNB_MYSQL_PWD')
hostname = os.getenv('HBNB_MYSQL_HOST')
datab = os.getenv('HBNB_MYSQL_DB')
type_st = os.getenv('HBNB_TYPE_STORAGE')


class DBStorage:
    """
    This class starts database engine
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                username,
                passw,
                datab),
            pool_pre_ping=True)
        if dev == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the current database session """
        a_dict = {}
        classes = [User, State, City, Place]

        if cls is None:
            for cl in classes:
                for instance in self.__session.query(cl).all():
                    key = cl.__name__ + "." + instance.id
                    a_dict[key] = instance
        else:
            for instance in self.__session.query(cls).all:
                key = cls.__name__ + "." + instance.id
                a_dict[key] = instance
        return a_dict

    def new(self, obj):
        """ adds object to the current database session """
        if obj:
            self.__session.add(obj)
            self.save()

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session obj """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ Creates all tables in the database
            Creates the current database session
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            expire_on_commit=False,
            bind=self.__engine))
        self.__session = Session()
