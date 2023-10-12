import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Interaction avec un curseur")

# Curseur
freq = st.slider("Choisissez une fréquence (Hz)", 1, 10, 5)

# Générer un signal sinusoïdal en fonction de la fréquence
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * freq * t)

# Afficher le graphique en fonction de la fréquence sélectionnée
st.line_chart(signal)
