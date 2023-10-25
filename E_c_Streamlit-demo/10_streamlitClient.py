import streamlit as st
import requests

# URL du serveur Flask
server_url = 'http://localhost:5000'  # Assurez-vous de mettre l'URL correcte

# Fonction pour récupérer des données depuis le serveur Flask
def get_server_data():
    response = requests.get(f'{server_url}/api/data')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Application Streamlit
st.title('Application Streamlit avec communication vers Flask')

# Bouton pour obtenir les données depuis le serveur
if st.button('Obtenir des données depuis le serveur'):
    server_data = get_server_data()
    if server_data:
        st.write('Données reçues depuis le serveur Flask:')
        st.json(server_data)
    else:
        st.write('Erreur lors de la récupération des données depuis le serveur.')

if __name__ == '__main__':
    st.write('Premier test API REST')
