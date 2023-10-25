import streamlit as st
import pandas as pd
import numpy as np
import time

# Créez une application Streamlit
st.title("Visualisation de données en temps réel")

# Créez un graphique à barres vide
chart = st.bar_chart([])

# Boucle pour la mise à jour en temps réel
while True:
    data = np.random.rand(10)  # Générez des données aléatoires (exemple)
    chart.bar_chart(data)  # Mettez à jour le graphique
    time.sleep(1)  # Attendez 1 seconde avant la prochaine mise à jour



