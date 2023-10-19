from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import Base

class Pays(Base):
    __tablename__ = "pays"

    id = Column(Integer, primary_key=True)
    pays = Column(String(255))