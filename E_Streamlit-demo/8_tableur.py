import streamlit as st
import pandas as pd
import json

st.title("Lecture et Affichage de Données depuis différents fichiers")

# Créez des onglets
onglet_selectionne = st.sidebar.radio("Sélectionnez un onglet :", ("Fichier CSV", "Fichier Excel", "Fichier JSON"))

# Onglet "Fichier CSV"
if onglet_selectionne == "Fichier CSV":
    st.header("Lecture de données depuis un fichier CSV")

    # Chargement des données depuis un fichier CSV
    file = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])
    if file is not None:
        data = pd.read_csv(file)

        # Affichez les données du fichier CSV
        st.dataframe(data)

# Onglet "Fichier Excel"
elif onglet_selectionne == "Fichier Excel":
    st.header("Lecture de données depuis un fichier Excel")

    # Chargement des données depuis un fichier Excel
    file = st.file_uploader("Téléchargez un fichier Excel", type=["xlsx"])
    if file is not None:
        data = pd.read_excel(file)

        # Affichez les données du fichier Excel
        st.dataframe(data)

# Onglet "Fichier JSON"
elif onglet_selectionne == "Fichier JSON":
    st.header("Lecture de données depuis un fichier JSON")

    # Chargement des données depuis un fichier JSON
    file = st.file_uploader("Téléchargez un fichier JSON", type=["json"])
    if file is not None:
        data = json.load(file)

        # Affichez les données du fichier JSON
        st.json(data)
