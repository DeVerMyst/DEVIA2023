import streamlit as st

st.title("Personnalisation des widgets")

# Personnaliser un widget bouton
button = st.button("Cliquez-moi")

# Utiliser du HTML pour personnaliser le bouton
button_html = """
<style>
    .stButton>button {
        background-color: green;
        color: white;
        border: 2px solid black;
        border-radius: 8px;
    }
</style>
"""
st.markdown(button_html, unsafe_allow_html=True)

if button:
    st.write("Vous avez cliqué sur le bouton !")
