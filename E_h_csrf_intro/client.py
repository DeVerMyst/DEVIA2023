import streamlit as st
import requests

# Fonction pour récupérer le token CSRF du serveur
def get_csrf_token():
    response = requests.get("http://localhost:5000/")
    csrf_token = response.json()["csrf_token"]
    return csrf_token

# Utiliser Streamlit pour créer une application web
def main():
    # Récupérer le token CSRF du serveur
    csrf_token = get_csrf_token()

    # Utiliser le token CSRF dans l'application Streamlit
    st.text_input("CSRF Token", value=csrf_token)

    # Autres éléments de l'interface utilisateur Streamlit
    # ...

if __name__ == "__main__":
    main()
