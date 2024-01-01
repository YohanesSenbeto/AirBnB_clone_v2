#!/usr/bin/env python3
"""
Defines a DBStorage engine.
"""

from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DBStorage:
    """
    Represents the database storage engine.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize a new DBStorage instance.
        """
        db_user = getenv("HBNB_MYSQL_USER")
        db_pwd = getenv("HBNB_MYSQL_PWD")
        db_host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(f"mysql+mysqldb://{db_user}:{db_pwd}@{db_host}/{db_name}?charset=utf8mb4",
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query all objects of a given class.
        """
        if cls is None:
            cls_list = [State, City, User, Place, Review, Amenity]
            objs = []
            for class_ in cls_list:
                objs.extend(self.__session.query(class_).all())
        else:
            objs = self.__session.query(cls).all() if isinstance(cls, type) else []

        return {f"{type(o).__name__}.{o.id}": o for o in objs}

    def new(self, obj):
        """
        Add obj to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit all changes to the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete obj from the current database session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Create all tables in the database and initialize a new session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Close the working SQLAlchemy session.
        """
        self.__session.close()

    def dbapi(cls):
        """
        Return the MySQL database API.
        """
        import MySQLdb as dbapi
        return dbapi

