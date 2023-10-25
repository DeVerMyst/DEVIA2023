import requests

# URL de l'API
BASE_URL = "http://localhost:8080/products"

# Envoi de la requête
response = requests.get(BASE_URL)

# Traitement de la réponse
if response.status_code == 200:
    products = response.json()
else:
    raise Exception(f"Erreur : {response.status_code}")

# Affichage des produits
for product in products:
    print(product["name"], product["price"])