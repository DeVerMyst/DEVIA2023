import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.table1 import Table1
from models.table2 import Table2

# Connexion à la base de données MySQL
engine = create_engine('mysql+mysqlconnector://root:root_password@db/sample_db')
Session = sessionmaker(bind=engine)
session = Session()

st.title('Application SQLAlchemy Streamlit')

# Création de la base de données si elle n'existe pas
if not engine.dialect.has_table(engine, "table1"):
    Base.metadata.create_all(engine)

# Interface utilisateur Streamlit
if st.button("Connect/Disconnect"):
    if st.session_state.db_connected:
        st.session_state.db_connected = False
        st.button_label = "Connect"
    else:
        st.session_state.db_connected = True
        st.button_label = "Disconnect"

st.write(f"Database Connection Status: {st.button_label}")

if st.session_state.db_connected:
    # Récupérer des données depuis la base de données
    result_sql = session.execute("SELECT * FROM table1")
    st.subheader("Using SQL Query")
    for row in result_sql:
        st.write(row)

    results_orm = session.query(Table1).all()
    st.subheader("Using SQLAlchemy ORM")
    for row in results_orm:
        st.write(row)

