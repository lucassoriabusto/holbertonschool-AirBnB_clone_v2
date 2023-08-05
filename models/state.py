#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import os  # Importa el módulo os para acceder a variables de entorno
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    """ Si estás utilizando DBStorage, agrega la relación con la clase City """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        """ Si estás utilizando FileStorage,
        agrega el getter attribute para las ciudades """
        @property
        def cities(self):
            """ Atributo getter que devuelve la lista de instancias de City
            con state_id igual al State.id actual """
            from models import storage
            city_instances = storage.all(City)
            matching_cities = []
            for city in city_instances.values():
                if city.state_id == self.id:
                    matching_cities.append(city)
            return matching_cities
