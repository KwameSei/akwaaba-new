#!/usr/bin/env python3
"""Module of user class"""
from datetime import datetime
from models.engine.database import Base
from sqlalchemy import Column, String, Text, Boolean, Integer, DateTime
#from models import storage_type
from sqlalchemy.orm import relationship


class User(Base):
    """Inherits from BaseModel class and adds user's functionalities"""
    __tablename__ = 'users'
    #if storage_type == 'db':
    id=Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    password = Column(Text, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone = Column(String(50), nullable=True)
    address = Column(String(100), nullable=True)
    status = Column(Boolean, default=True)
    all_events = relationship('All_Event', back_populates='user')
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
        #events = relationship("Event", backref="user")

    # Return string representation of the module
    def __repr__(self):
        return f"<User id={self.id} email={self.email} first_name={self.first_name}\
            last_name={self.last_name} phone={self.phone} address={self.address} status={self.status}>"
    
    def to_dict(self):
        event_dict = {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone": self.phone,
            "address": self.address,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        return event_dict