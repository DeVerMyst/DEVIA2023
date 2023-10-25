import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Créez une application Streamlit
st.title("Outil d'analyse de données interactif")

# Sélectionnez un fichier CSV à charger
uploaded_file = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Affichage des données
    st.header("Aperçu des données")
    st.write(data.head())

    # Statistiques descriptives
    st.header("Statistiques descriptives")
    st.write(data.describe())

    # Choix des colonnes à afficher
    selected_columns = st.multiselect("Sélectionnez les colonnes à afficher :", data.columns)

    if selected_columns:
        st.write(data[selected_columns])

    # Affichage d'un graphique interactif
    st.header("Graphique interactif")
    selected_x = st.selectbox("Sélectionnez la variable X :", data.columns)
    selected_y = st.selectbox("Sélectionnez la variable Y :", data.columns)

    if selected_x and selected_y:
        fig, ax = plt.subplots()
        sns.scatterplot(data=data, x=selected_x, y=selected_y, ax=ax)
        st.pyplot(fig)

    # Filtrage des données
    st.header("Filtrage des données")
    selected_column = st.selectbox("Sélectionnez une colonne pour le filtrage :", data.columns)
    unique_values = data[selected_column].unique()
    selected_value = st.selectbox("Sélectionnez une valeur :", unique_values)

    if selected_value:
        filtered_data = data[data[selected_column] == selected_value]
        st.write(filtered_data)

    # Ajout d'un histogramme
    st.header("Histogramme")
    selected_numeric_column = st.selectbox("Sélectionnez une colonne numérique :", data.select_dtypes("number").columns)
    num_bins = st.slider("Nombre de bacs", min_value=5, max_value=50)
    
    # Par cette ligne
    fig, ax = plt.subplots()
    hist = plt.hist(data[selected_numeric_column], bins=num_bins, edgecolor="k")
    st.pyplot(fig)

    # Résumé des données
    st.header("Résumé des données")
    st.write(data.info())
