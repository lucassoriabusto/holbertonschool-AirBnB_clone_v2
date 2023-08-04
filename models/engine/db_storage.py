#!/usr/bin/python3
from os import getenv
import MySQLdb
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import Base

class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None


    def new(self, obj):
        """create a new"""
        self.__session.add(obj)

    def save(self):
        """create a save"""
        self.__session.commit()

    def delete(self, obj=None):
        """deleta a delete"""
        if obj is not None:
            self.session.delete(obj)

    def reload(self):
       """Reload"""
       Base.metadata.create_all(self.__engine)
       current_session = sessionmaker(self.__engine, expire_on_commit=False)
       self.__session = scoped_session(current_session)