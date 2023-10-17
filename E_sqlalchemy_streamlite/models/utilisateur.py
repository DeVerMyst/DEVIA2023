from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import Base

class Utilisateur(Base):
    __tablename__ = "utilisateur"

    id = Column(Integer, primary_key=True)
    nom = Column(String(255))
    prenom = Column(String(255))
    mail = Column(String(255))

    genre_id = Column(Integer, ForeignKey("genre.id"))
    genre = relationship("Genre")

    pays_id = Column(Integer, ForeignKey("pays.id"))
    pays = relationship("Pays")