#!/usr/bin/env python3
"""Event module for Akwaaba project"""

from datetime import datetime
from models.engine.database import Base
#from models import storage_type
from sqlalchemy import Column, String, ForeignKey, DateTime, Float, Text, Boolean, Integer
from sqlalchemy.orm import relationship

class All_Event(Base):
    """The event class"""
    __tablename__ = 'all_events'
    #if storage_type == 'db':
    id=Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    category = Column(String(50), nullable=False)
    start_date = Column(String(30), nullable=True)
    end_date = Column(String(30), nullable=True)
    location = Column(String(50), nullable=False)
    region = Column(String(50), nullable=False)
    cost = Column(Integer, default=0, nullable=True)
    registration = Column(Boolean, nullable=True)
    isPublic = Column(Boolean, nullable=False)
    views = Column(Integer, default=0)
    featuredImage = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    user = relationship('User', back_populates='all_events')
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"All_Event('{self.id}','{self.title}', '{self.description}', '{self.category}', '{self.start_date}', '{self.end_date}', '{self.location}', '{self.region}' '{self.cost}', '{self.registration}', '{self.isPublic}', '{self.views}', '{self.created_at}', '{self.updated_at}')"

    # def to_dict(self):
    #     # Convert the All_Event object to a dictionary
    #     event_dict = self.__dict__
    #     event_dict.pop('_sa_instance_state', None)
    #     return event_dict

    def to_dict(self):
        event_dict = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "location": self.location,
            "region": self.region,
            "cost": self.cost,
            "featuredImage": self.featuredImage,
            "registration": self.registration,
            "isPublic": self.isPublic,
            "views": self.views,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user_id": self.user_id
        }
        return event_dict

    # Return string representation of the module
    # def __repr__(self):
    #     return f"<All_Event id={self.id} title={self.title} description={self.description}\
    #         start_date={self.start_date} end_date={self.end_date} location={self.location}\
    #         isPublic={self.isPublic} views={self.views}>"