from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy import create_engine
from models.base import Base
import streamlit as st

import logging

# Création de la connexion à la base de données
def create_db():
    engine = create_engine("mysql+pymysql://root:root_password@localhost/sample_db")

    if database_exists(engine.url):
        drop_database(engine.url)    

    create_database(engine.url)

    # if database_exists(engine.url):
    #     st.write(f"Database Connection Status: Connected")

    # Création des tables
    Base.metadata.create_all(engine)
    return engine 