#!/usr/bin/python3
"""State class"""
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import models
from models.base_model import BaseModel, Base
import shlex
from models.city import City



class State(BaseModel, Base):
    """State class
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        m_var = models.storage.all()
        list_a = []
        res = []
        for k in m_var:
            city = k.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                list_a.append(m_var[k])
        for element in list_a:
            if (element.state_id == self.id):
                res.append(element)
        return (res)
