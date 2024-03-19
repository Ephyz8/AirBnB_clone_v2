#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from models.amenity import Amenity
from models.base_model import Base
from models.place import Place
from models.city import City
from models.user import User
from models.review import Review
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (create_engine)


class DBStorage:
    """Creates tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        data_base = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        envm = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, data_base),
                                      pool_pre_ping=True)

        if envm == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        m_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elements in query:
                k = "{}.{}".format(type(elements).__name__, elements.id)
                m_dict[k] = elements
        else:
            list_a = [State, City, User, Place, Review, Amenity]
            for clase in list_a:
                query = self.__session.query(clase)
                for elements in query:
                    k = "{}.{}".format(type(elements).__name__, elements.id)
                    m_dict[k] = elements
        return (m_dict)

    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()
