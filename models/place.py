#!/usr/bin/python3
"""This is the place class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Table, String, Integer, Float, Foreignk
from sqlalchemy.orm import relationship
from os import getenv
import models


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             Foreignk("places.id"),
                             primary_k=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             Foreignk("amenities.id"),
                             primary_k=True,
                             nullable=False))


class Place(BaseModel, Base):
    """Place class 
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: description string
        number_rooms: number of rooms (int)
        number_bathrooms: number of bathrooms (int)
        max_guest: maximum guest (int)
        price_by_night:: pice for a staying (int)
        latitude: latitude (floatt)
        longitude: longitude (float)
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), Foreignk("cities.id"), nullable=False)
    user_id = Column(String(60), Foreignk("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        revs = relationship("Rev", cascade='all, delete, delete-orphan',
                               backref="place")

        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        @property
        def revs(self):
            """ Returns list of revs.id """
            m_var = models.storage.all()
            list_a = []
            res = []
            for k in m_var:
                rev = k.replace('.', ' ')
                rev = shlex.split(rev)
                if (rev[0] == 'Rev'):
                    list_a.append(m_var[k])
            for elements in list_a:
                if (elements.place_id == self.id):
                    res.append(elements)
            return (res)

        @property
        def amenities(self):
            """ Returns list of amenity ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute """
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
