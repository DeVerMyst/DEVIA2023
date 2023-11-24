# model.py
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

# Création de la base de données
engine = create_engine('sqlite:///app.db')
Base.metadata.create_all(bind=engine)

# Création d'une session SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()
