from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy import create_engine
from models.base import Base
import streamlit as st

import logging

# Création de la connexion à la base de données
def create_db():
    engine = create_engine("mysql+pymysql://root:root@localhost/dbstream")

    if database_exists(engine.url):
        drop_database(engine.url)    

    create_database(engine.url)

    FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT)
    d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    logger = logging.getLogger('tcpserver')
    logger.warning('Protocol problem: %s', 'connection reset', extra=d)

    if database_exists(engine.url):
        st.write(f"Database Connection Status: Connected")

    # Création des tables
    Base.metadata.create_all(engine)
    return engine 