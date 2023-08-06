#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Reviews"""
            from models import storage
            from models.review import Review

            list = []
            for x in storage.all(Review):
                if x.place_id == self.id:
                    list.append(x)
            return list

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity

            amenity_instances = []
            for amenity_id in self.amenity_ids:
                amenity_instance = storage.get(Amenity, amenity_id)
                if amenity_instance is not None:
                    amenity_instances.append(amenity_instance)
            return amenity_instances

        @amenities.setter
        def amenities(self, amenity_obj):
            from models.amenity import Amenity

            if isinstance(amenity_obj, Amenity):
                if amenity_obj.id not in self.amenity_ids:
                    self.amenity_ids.append(amenity_obj.id)
