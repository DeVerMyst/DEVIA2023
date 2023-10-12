import streamlit as st

st.title("Tableau de bord avec onglets")

# Créez des onglets
tabs = st.sidebar.radio("Sélectionnez un onglet :", ("Onglet 1", "Onglet 2", "Onglet 3"))

if tabs == "Onglet 1":
    st.header("Onglet 1")
    st.write("Contenu de l'onglet 1")

elif tabs == "Onglet 2":
    st.header("Onglet 2")
    st.write("Contenu de l'onglet 2")

elif tabs == "Onglet 3":
    st.header("Onglet 3")
    st.write("Contenu de l'onglet 3")
