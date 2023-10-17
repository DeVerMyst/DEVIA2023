import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect

from components.create_db import create_db
from models.genre import Genre
from models.pays import Pays
from models.utilisateur import Utilisateur

st.title('Application SQLAlchemy Streamlit')

# creation de la base de données
engine = create_db()
# Création d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Formulaire d'ajout d'utilisateur
st.subheader("Add User to Database")
username = st.text_input("Username:")
genre_name = st.text_input("Genre:")
pays_name = st.text_input("Pays:")

if st.button("Add User"):
    # Recherche du genre dans la base de données ou création s'il n'existe pas
    genre = session.query(Genre).filter_by(name=genre_name).first()
    if genre is None:
        Genre = Genre(name=genre_name)
        session.add(Genre)
        session.commit()

    # Recherche de la ville dans la base de données ou création s'il n'existe pas
    city = session.query(Pays).filter_by(name=pays_name).first()
    if city is None:
        city = Pays(name=pays_name)
        session.add(city)
        session.commit()

    # Ajout de l'utilisateur à la base de données
    user = Utilisateur(username=username, Genre_id=Genre.id, city_id=city.id)
    session.add(user)
    session.commit()

    st.success("User added to the database.")

# Affichage des données d'utilisateurs
result_sql = session.query(Utilisateur, Genre, Pays).join(Genre).join(Pays)
st.subheader("Users in the Database")
for user, Genre, city in result_sql:
    st.write(f"User: {user.username}, Genre: {Genre.name}, City: {city.name}")
