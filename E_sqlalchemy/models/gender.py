from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Gender(Base):
    __tablename__ = 'genders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    users = relationship('User', back_populates='gender')

    def __init__(self, name):
        self.name = name
