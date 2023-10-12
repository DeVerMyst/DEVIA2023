import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Créez une application Streamlit
st.title("Tableau de bord pour l'apprentissage automatique")

# Chargement des données
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Séparation des données en ensemble d'entraînement et ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Création et entraînement du modèle
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Prédiction sur l'ensemble de test
y_pred = clf.predict(X_test)

# Affichage de la précision du modèle
accuracy = accuracy_score(y_test, y_pred)
st.write(f"Précision du modèle : {accuracy:.2f}")

# Affichage du rapport de classification
report = classification_report(y_test, y_pred, target_names=data.target_names)
st.text("Rapport de classification :")
st.text(report)

# Créez une section pour l'affichage des données
st.header("Données d'entraînement et de test")
st.write("Données d'entraînement :")
st.write(X_train)
st.write("Données de test :")
st.write(X_test)

# Affichage d'un graphique
st.header("Graphique")
st.bar_chart(data.data)
