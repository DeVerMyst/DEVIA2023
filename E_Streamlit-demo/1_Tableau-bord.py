import streamlit as st

st.title("Tableau de bord simple")

# Ajouter un widget bouton
if st.button("Cliquez-moi"):
    st.write("Vous avez cliqué sur le bouton !")

# Ajouter un widget curseur
age = st.slider("Choisissez votre âge", 0, 100, 25)
st.write(f"Vous avez {age} ans.")
