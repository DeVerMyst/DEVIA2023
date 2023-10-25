import streamlit as st
import sqlite3

st.title("Connexion à une base de données SQL (SQLite)")

# Connexion à la base de données SQLite
conn = sqlite3.connect('ma_base_de_donnees.db')
cursor = conn.cursor()

# Création d'une table (si elle n'existe pas)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INTEGER PRIMARY KEY,
        nom TEXT,
        email TEXT
    )
''')
conn.commit()

# Formulaire pour ajouter un nouvel utilisateur
st.subheader("Ajouter un nouvel utilisateur")
nom = st.text_input("Nom")
email = st.text_input("Email")

if st.button("Ajouter"):
    cursor.execute("INSERT INTO utilisateurs (nom, email) VALUES (?, ?)", (nom, email))
    conn.commit()
    st.success("Utilisateur ajouté avec succès.")

# Affichage des utilisateurs existants
st.subheader("Liste des utilisateurs")
utilisateurs = cursor.execute("SELECT id, nom, email FROM utilisateurs").fetchall()
for utilisateur in utilisateurs:
    st.write(utilisateur)

# Fermeture de la connexion à la base de données
conn.close()
