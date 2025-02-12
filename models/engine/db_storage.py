#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base

class DBStorage:
    """Database storage engine using SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database storage engine"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{database}',
            pool_pre_ping=True
        )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects or specific class objects from database"""
        from models import storage_classes
        obj_dict = {}
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = []
            for class_name in storage_classes.values():
                objects.extend(self.__session.query(class_name).all())

        for obj in objects:
            key = f"{obj.__class__.__name__}.{obj.id}"
            obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Add new object to database session"""
        self.__session.add(obj)

    def save(self):
        """Commit changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create database tables and session"""
        from models.base_model import Base
        from models import storage_classes
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Remove the current session"""
        self.__session.remove()
