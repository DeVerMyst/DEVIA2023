import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
import pandas as pd

st.title("Application avec Onglets")

# Créez des onglets
onglet_selectionne = st.sidebar.radio("Sélectionnez un onglet :", ("Matplotlib", "Plotly", "Altair"))

# Onglet "Matplotlib"
if onglet_selectionne == "Matplotlib":
    st.header("Graphique à barres avec Matplotlib")
    
    # Données pour le graphique
    categories = ['Catégorie A', 'Catégorie B', 'Catégorie C']
    valeurs = [5, 8, 12]
    
    # Créez le graphique à barres avec Matplotlib
    fig, ax = plt.subplots()
    ax.bar(categories, valeurs)
    
    # Affichez le graphique
    st.pyplot(fig)

# Onglet "Plotly"
elif onglet_selectionne == "Plotly":
    st.header("Graphique à barres interactif avec Plotly")
    
    # Données pour le graphique
    data = {'Categories': ['A', 'B', 'C'],
            'Valeurs': [5, 8, 12]}
    
    # Créez un graphique à barres interactif avec Plotly
    fig = px.bar(data, x='Categories', y='Valeurs', title="Graphique interactif à barres")
    
    # Affichez le graphique
    st.plotly_chart(fig)

# Onglet "Altair"
elif onglet_selectionne == "Altair":
    st.header("Graphique à barres avec Altair")
    
    # Données pour le graphique
    data = pd.DataFrame({'Categories': ['A', 'B', 'C'], 'Valeurs': [5, 8, 12]})
    
    # Créez le graphique à barres avec Altair
    chart = alt.Chart(data).mark_bar().encode(
        x='Categories',
        y='Valeurs'
    ).properties(
        width=400
    )
    
    # Affichez le graphique
    st.altair_chart(chart)
