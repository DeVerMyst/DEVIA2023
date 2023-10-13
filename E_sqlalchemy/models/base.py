from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Remplacez 'mysql+mysqlconnector://root:root_password@db/sample_db' par votre URL de connexion MySQL
db_url = 'mysql+mysqlconnector://root:root_password@db/sample_db'
engine = create_engine(db_url, echo=True)  # Utilisez "echo=True" pour afficher les requêtes SQL

Base = declarative_base()
