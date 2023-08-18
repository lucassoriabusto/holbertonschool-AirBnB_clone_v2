#!/usr/bin/python3
"""Contains DBStorage storage class"""
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

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Return the table"""
        from console import HBNBCommand

        data = {}
        if cls in HBNBCommand.classes.values():
            result = self.__session.query(cls).all()
            for x in result:
                data[f"{cls.__name__}.{x.id}"] = x.to_dict()

        else:
            for table in HBNBCommand.classes.values():
                if table.__name__ != 'BaseModel':
                    result = self.__session.query(table).all()
                    for x in result:
                        string = f"{table.__class__.__name__}.{x.id}"
                        data[string] = x.to_dict()

        return data

    def new(self, obj):
        """create a new"""
        self.__session.add(obj)

    def save(self):
        """create a save"""
        self.__session.commit()

    def delete(self, obj=None):
        """deleta a delete"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload"""
        Base.metadata.create_all(self.__engine)
        current_session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = scoped_session(current_session)

    def close(self):
        self.__session.remove()
