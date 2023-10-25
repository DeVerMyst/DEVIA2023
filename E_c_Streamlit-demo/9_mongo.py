import streamlit as st
import pymongo

st.title("Connexion à une base de données NoSQL (MongoDB)")

# Connexion à la base de données MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ma_base_de_donnees"]
collection = db["utilisateurs"]

# Formulaire pour ajouter un nouvel utilisateur
st.subheader("Ajouter un nouvel utilisateur")
nom = st.text_input("Nom")
email = st.text_input("Email")

if st.button("Ajouter"):
    nouvel_utilisateur = {
        "nom": nom,
        "email": email
    }
    collection.insert_one(nouvel_utilisateur)
    st.success("Utilisateur ajouté avec succès.")

# Affichage des utilisateurs existants
st.subheader("Liste des utilisateurs")
utilisateurs = collection.find()
for utilisateur in utilisateurs:
    st.write(utilisateur)

# Fermeture de la connexion à la base de données
client.close()
