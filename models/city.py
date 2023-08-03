#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    state_id = Column(String(60), ForeignKey("state.id"), nullable=False)
    name = Column(String(60), nullable=False)

    places = relationship("Place", cascade="all, delete", backref="cities")
