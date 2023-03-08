#!/usr/bin/env python3
"""Event module for Akwaaba project"""

from models.engine.database import Base
#from models import storage_type
from sqlalchemy import Text, Column, Integer, String, LargeBinary

class Images(Base):
    """The event class"""
    __tablename__ = 'images'
    #if storage_type == 'db':
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    mimetype = Column(String(64), nullable=False)
    img = Column(LargeBinary(length=(2**32)-1), nullable=False)