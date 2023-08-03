#!/usr/bin/python3
""" Place Module for HBNB project """

from models.base_model import BaseModel
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = []



