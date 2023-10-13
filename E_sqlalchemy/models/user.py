from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    gender_id = Column(Integer, ForeignKey('genders.id'))
    city_id = Column(Integer, ForeignKey('cities.id'))

    gender = relationship('Gender', back_populates='users')
    city = relationship('City', back_populates='users')

    def __init__(self, username, gender_id, city_id):
        self.username = username
        self.gender_id = gender_id
        self.city_id = city_id
