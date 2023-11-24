import streamlit as st
import requests

# Utiliser Streamlit pour créer une application web
def main():
    # Ne pas récupérer le token CSRF lors de la méthode GET
    st.text("Client sans récupération de token CSRF lors de la méthode GET")

    # Simuler une requête POST sans token CSRF
    if st.button("Envoyer requête POST sans token CSRF"):
        response = requests.post("http://localhost:5000/")
        st.text(f"Réponse du serveur: {response.text}")

if __name__ == "__main__":
    main()
