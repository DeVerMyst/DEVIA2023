from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)

    users = relationship('User', back_populates='city')

    def __init__(self, name):
        self.name = name
