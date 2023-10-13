import streamlit as st

st.title("Widgets Streamlit")

# Bouton
if st.button("Cliquez-moi"):
    st.write("Vous avez cliqué sur le bouton !")

# Curseur
age = st.slider("Choisissez votre âge", 0, 100, 25)
st.write(f"Vous avez {age} ans.")

# Zone de texte
name = st.text_input("Entrez votre nom")
st.write(f"Bonjour, {name} !")

# Cases à cocher
if st.checkbox("Montrez les détails"):
    st.write("Les détails sont affichés.")
