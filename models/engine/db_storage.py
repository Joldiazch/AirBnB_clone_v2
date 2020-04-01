#!usr/bin/python3
""" DataBase storage """
import sys
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import os

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
        Base.metadata.create_all(self.__engine)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(bind=self.__engine, tables=[username.__table__])

    def all(self, cls=None):
        """ query on the current database session """
        a_dict = {}
        classes = ["User", "State", "City", "Amenity", "Place", "Review"]
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

        if cls=None:
            for cl in classes:
                cols = eval(cl).__table__.columns.keys()
                for instance in self.__session.query(cl).all:
                    key = cl + "." + instance.id
                    a_dict[key] = {col: eval('instance.' + col) for col in cols}
        else:
            cols = cls.__table__.columns.keys()
            for instance in self.__session.query(cls).all:
                key = cls.__name__ + "." + instance.id
                a_dict[key] = {col: eval('instance.' + col) for col in cols}
