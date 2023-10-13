import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from sqlalchemy import inspect
from models.user import User
from models.gender import Gender
from models.city import City


engine = create_engine('mysql+mysqlconnector://root:root_password@localhost/sample_db?charset=utf8mb4')


Session = sessionmaker(bind=engine)
session = Session()


st.title('Application SQLAlchemy Streamlit')



# # Création de la base de données si elle n'existe pas
# if not inspect(engine).has_table("users"):

#     Base.metadata.create_all(engine)

# st.write(f"Database Connection Status: Connected")

# # Formulaire d'ajout d'utilisateur
# st.subheader("Add User to Database")
# username = st.text_input("Username:")
# gender_name = st.text_input("Gender:")
# city_name = st.text_input("City:")

# if st.button("Add User"):
#     # Recherche du genre dans la base de données ou création s'il n'existe pas
#     gender = session.query(Gender).filter_by(name=gender_name).first()
#     if gender is None:
#         gender = Gender(name=gender_name)
#         session.add(gender)
#         session.commit()

#     # Recherche de la ville dans la base de données ou création s'il n'existe pas
#     city = session.query(City).filter_by(name=city_name).first()
#     if city is None:
#         city = City(name=city_name)
#         session.add(city)
#         session.commit()

#     # Ajout de l'utilisateur à la base de données
#     user = User(username=username, gender_id=gender.id, city_id=city.id)
#     session.add(user)
#     session.commit()

#     st.success("User added to the database.")

# # Affichage des données d'utilisateurs
# result_sql = session.query(User, Gender, City).join(Gender).join(City)
# st.subheader("Users in the Database")
# for user, gender, city in result_sql:
#     st.write(f"User: {user.username}, Gender: {gender.name}, City: {city.name}")
