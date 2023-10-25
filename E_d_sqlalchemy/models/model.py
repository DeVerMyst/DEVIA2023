# Importez les modules SQLAlchemy et définissez votre modèle de base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Définissez vos classes de modèle
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

class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    nom = Column(String(255))

class Pays(Base):
    __tablename__ = "pays"

    id = Column(Integer, primary_key=True)
    nom = Column(String(255))
