import streamlit as st
import numpy as np

st.title("Interaction avec un curseur")

# Curseur
freq = st.slider("Choisissez une fréquence (Hz)", 64, 512, 64)

# Générer un signal sinusoïdal en fonction de la fréquence
Fs = 1024
t = np.linspace(0, 1/64, Fs)
signal = np.sin(2 * np.pi * freq * t)

# Afficher le graphique en fonction de la fréquence sélectionnée
st.line_chart(signal)


