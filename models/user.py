#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from models.review import Review
from sqlalchemy.orm import relationship
from models.place import Place
from sqlalchemy import Column, Integer, String



class User(BaseModel, Base):
    """User class
    Attributes:
        email: email address
        passwd: passwd for login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    passwd = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
