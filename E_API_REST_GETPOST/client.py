import streamlit as st
import requests
import json

# URL du serveur
BASE_URL = "http://localhost:8080/"

# Titre de la page
st.title("API REST avec Flask et Streamlit")


def get_route(): 
    response = requests.get(BASE_URL + "route")
    if response.status_code == 200:
        st.write( json.loads(response.text)["route"] )
    
def post_route(): 
    response = requests.post(BASE_URL + "route")    
    if response.status_code == 200:
        st.write( json.loads(response.text)["route"] )

def put_route(): 
    response = requests.put(BASE_URL + "route")    
    if response.status_code == 200:
        st.write( json.loads(response.text)["route"] )

def delete_route(): 
    response = requests.delete(BASE_URL + "route")    
    if response.status_code == 200:
        st.write( json.loads(response.text)["route"] )

col1, col2, col3, col4 = st.columns(4)

with col1:
    # Boutons pour les méthodes GET 
    st.button("HTTP GET", on_click=get_route)
with col2:    
    # Boutons pour les méthodes POST 
    st.button("HTTP POST", on_click=post_route)
with col3:
    # Boutons pour les méthodes PUT
    st.button("HTTP PUT", on_click=put_route)
with col4:    
    # Boutons pour les méthodes DELETE
    st.button("HTTP DELETE", on_click=delete_route)



# Fonction pour récupérer les produits
def get_products():
    response = requests.get(BASE_URL + "products")

    if response.status_code == 200:
        products = json.loads(response.text)

        st.table(products)
    else:
        st.error(f"Erreur : {response.status_code}")

# Formulaire pour créer un nouveau produit
with st.form("create_product_form"):
    product_name = st.text_input("Nom du produit")
    product_price = st.number_input("Prix du produit")

    # Soumission du formulaire
    if st.form_submit_button():
        if product_name and product_price:
            product_data = {
                "name": product_name,
                "price": product_price
            }

            response = requests.post(BASE_URL + "products", json=product_data)

            if response.status_code == 201:
                product = json.loads(response.text)

                st.success(f"Nouveau produit créé : {product}")
                

            else:
                st.error(f"Erreur : {response.status_code}")

get_products()


