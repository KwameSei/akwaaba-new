# #!/usr/bin/env python3
# """Module of user class"""
# from models.engine.database import Base
# from sqlalchemy import Column, String, Text, Boolean, Integer, Float, ForeignKey
# #from models import storage_type
# from sqlalchemy.orm import relationship


# class User(Base):
#     """Inherits from BaseModel class and adds user's functionalities"""
#     __tablename__ = 'users'
#     #if storage_type == 'db':
#     id=Column(Integer, primary_key=True, autoincrement=True)
#     email = Column(String(100), nullable=False)
#     password = Column(Text, nullable=False)
#     first_name = Column(String(100), nullable=False)
#     last_name = Column(String(100), nullable=False)
#     phone = Column(String(50), nullable=True)
#     address = Column(String(100), nullable=True)
#     status = Column(Boolean, default=True)
#     all_events = relationship('All_Event', back_populates='user')
#         #events = relationship("Event", backref="user")

#     def __repr__(self):
#         return f"<User id={self.id} email={self.email} first_name={self.first_name}\
#             last_name={self.last_name} phone={self.phone} address={self.address} status={self.status}>"

# class All_Event(Base):
#     """The event class"""
#     __tablename__ = 'all_events'
#     #if storage_type == 'db':
#     id=Column(Integer, primary_key=True, autoincrement=True)
#     title = Column(String(50), nullable=False, unique=True)
#     description = Column(Text, nullable=False)
#     category = Column(String(50), nullable=False)
#     start_date = Column(String(30), nullable=True)
#     end_date = Column(String(30), nullable=True)
#     location = Column(String(50), nullable=False)
#     region = Column(String(50), nullable=False)
#     cost = Column(Float, default=0, nullable=True)
#     registration = Column(Boolean, nullable=True)
#     isPublic = Column(Boolean, nullable=False)
#     views = Column(Integer, default=0)
#     user = relationship('User', back_populates='all_events')
#     user_id = Column(Integer, ForeignKey('users.id'))

#     def __repr__(self):
#         return f"<All_Event id={self.id} title={self.title} description={self.description}\
#             start_date={self.start_date} end_date={self.end_date} location={self.location}\
#             region={self.region} cost={self.cost} registration={self.registration}\
#             isPublic={self.isPublic} views={self.views}>"
