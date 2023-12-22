# client.py

import requests

# URL de l'API
api_url = 'http://127.0.0.1:5000'

# Endpoint pour obtenir la liste des utilisateurs
users_endpoint = '/users'

# Endpoint pour obtenir un utilisateur par son ID
user_endpoint = '/user/1'  # Changez l'ID en fonction de votre base de données

# Envoi d'une requête GET pour obtenir la liste des utilisateurs
response = requests.get(api_url + users_endpoint)
print("Liste des utilisateurs:", response.json())

# Envoi d'une requête GET pour obtenir un utilisateur spécifique par son ID
response = requests.get(api_url + user_endpoint)
print("Utilisateur spécifique:", response.json())
