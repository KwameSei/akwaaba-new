#!/usr/bin/python3
"""Managing database storage for Akwaaba"""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session, sessionmaker
from models.user import User
from models.event import Event


class DB_storage:
    """Database storage engine for mysql"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate new db storage instance"""
        MYSQL_USER = getenv("MYSQL_USER")
        MYSQL_PWD = getenv("MYSQL_PWD")
        MYSQL_HOST = getenv("MYSQL_HOST")
        MYSQL_DB = getenv("MYSQL_DB")
        ENV = getenv("ENV")

        # self.__engine = create_engine(
        #     "mysql+mysqldb://{}:{}@{}/{}".format(
        #                                   MYSQL_USER,
        #                                   MYSQL_PWD,
        #                                   MYSQL_HOST,
        #                                   MYSQL_DB
        #     ), pool_pre_ping=True
        # )

        if ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)"""
        obj_dict = {}

        if cls is None:
            classes = {'Event': Event, 'User': User}

            for key, value in classes.items():
                all_obj = self.__session.query(value).all()

                for one_obj in all_obj:
                    key = "{}.{}".format(type(one_obj).__name__, one_obj.id)
                    obj_dict[key] = one_obj
        else:
            if type(cls) == str:
                cls = eval(cls)
                all_obj = self.__session.query(cls)
                for one_obj in all_obj:
                    key = one_obj.__class__.__name__ + '.' + one_obj.id
                    obj_dict[key] = one_obj
        return obj_dict

    def new(self, one_obj):
        """Adds new object to the current database session"""
        self.__session.add(one_obj)

    def save(self):
        """Commits all changes to the current database"""
        self.__session.commit()

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def delete(self, one_obj=None):
        """Deletes from the current database"""
        if (one_obj):
            self.__session.delete(one_obj)
        else:
            pass

    def close(self):
        """Closing the session"""
        self.__session.close()