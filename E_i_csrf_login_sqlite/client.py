# client.py
import streamlit as st
import requests

def get_csrf_token():
    response = requests.get("http://localhost:5000/")
    
    # Ajoutez la vérification pour s'assurer que la réponse est un JSON valide
    try:
        csrf_token = response.json()["csrf_token"]
        return csrf_token
    except (KeyError, ValueError) as e:
        print(f"Erreur lors de l'extraction du token CSRF : {e}")
        return None


def create_user(username, email, csrf_token):
    data = {"username": username, "email": email, "csrf_token": csrf_token}
    response = requests.post("http://localhost:5000/", json=data)
    return response.json()

def get_users():
    response = requests.get("http://localhost:5000/users")
    return response.json()["users"]

def main():
    st.title("Application Client")

    csrf_token = get_csrf_token()

    st.subheader("Créer un nouvel utilisateur")
    username = st.text_input("Nom d'utilisateur")
    email = st.text_input("Email")

    if st.button("Créer utilisateur"):
        result = create_user(username, email, csrf_token)
        st.text(result["message"])

    st.subheader("Liste des utilisateurs")
    try:
        users = get_users()
        for user in users:
            st.text(f"ID: {user['id']}, Username: {user['username']}, Email: {user['email']}")
    except (KeyError, ValueError) as e:
        print(f"Erreur lors de l'affichage des clients : {e}")

if __name__ == "__main__":
    main()
