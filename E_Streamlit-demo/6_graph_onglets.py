import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import folium

st.title("Application avec onglets")

# Créez des onglets
tabs = st.sidebar.radio("Sélectionnez un onglet :", ("Graphique à barres", "Graphique circulaire", "Carte"))

# Onglet "Graphique à barres"
if tabs == "Graphique à barres":
    st.header("Graphique à barres interactif")
    
    # Données pour le graphique à barres
    categories = ['Catégorie A', 'Catégorie B', 'Catégorie C']
    valeurs = [5, 8, 12]
    
    # Créez le graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(categories, valeurs)
    
    # Affichez le graphique
    st.pyplot(fig)

# Onglet "Graphique circulaire"
elif tabs == "Graphique circulaire":
    st.header("Graphique circulaire interactif")
    
    # Données pour le graphique circulaire
    data = {'Labels': ['A', 'B', 'C', 'D'],
            'Valeurs': [25, 30, 15, 10]}
    
    # Créez un graphique circulaire interactif avec Plotly
    fig = px.pie(data, names='Labels', values='Valeurs')
    
    # Affichez le graphique
    st.plotly_chart(fig)

# Onglet "Carte"
elif tabs == "Carte":
    st.header("Carte interactive")
    
    # Créez une carte avec Folium
    m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)

    # Ajoutez un marqueur à la carte
    folium.Marker([51.5074, -0.1278], tooltip='Londres').add_to(m)

    # Affichez la carte dans Streamlit
    st.write(m._repr_html_(), unsafe_allow_html=True)