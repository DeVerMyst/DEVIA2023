from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import Base

class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    genre = Column(String(255))