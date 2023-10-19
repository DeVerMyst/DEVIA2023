import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from sqlalchemy_utils import database_exists

from components.create_db import create_db

import pandas as pd

from models.genre import Genre
from models.pays import Pays
from models.utilisateur import Utilisateur

st.title('Application SQLAlchemy Streamlit')

# creation de la base de données
engine = create_db()

if database_exists(engine.url):
    st.write(f"Database Connection Status: Connected")
else: 
    st.write(f"Database Connection Status: Disconnected")
# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Formulaire d'ajout d'utilisateur
st.subheader("Add User to Database")
nom = st.text_input("Nom:")
genre_name = st.text_input("Genre:")
pays_name = st.text_input("Pays:")

if st.button("Add User"):
    # Recherche du genre dans la base de données ou création s'il n'existe pas
    genre_n = session.query(Genre).filter_by(genre=genre_name).first()
    if genre_n is None:
        genre_ = Genre(genre=genre_n)
        session.add(genre_)
        session.commit()

    # Recherche de la ville dans la base de données ou création s'il n'existe pas
    pays_n = session.query(Pays).filter_by(pays=pays_name).first()
    if pays_n is None:
        pays_ = Pays(pays=pays_n)
        session.add(pays_)
        session.commit()

    # Ajout de l'utilisateur à la base de données
    user = Utilisateur(nom=nom, genre_id=genre_.id, pays_id=pays_.id)
    session.add(user)
    session.commit()

    st.success("User added to the database.")

    # Affichage des données d'utilisateurs
    result_sql = session.query(
        Utilisateur, 
        Genre, 
        Pays).join(
            Genre, 
            Utilisateur.genre_id == Genre.id).join(
                Pays, 
                Utilisateur.pays_id == Pays.id).all()
    if result_sql:
        st.subheader("Users in the Database")
        for user_as, genre_as, pays_as in result_sql:
            df = pd.DataFrame({"User": user_as.nom, "Genre": genre_as.genre, "City": pays_as.pays}) 
            st.dataframe(data)
            # st.write(f"User: {user_as.nom}, Genre: {genre_as.genre}, City: {pays_as.pays}")
