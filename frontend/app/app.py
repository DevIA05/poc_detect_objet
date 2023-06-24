# Package ----------------------------------------------------------------------
import streamlit as st
# Configuration ----------------------------------------------------------------
# Titre de l'application
st.title("Ma première application Streamlit")
# Texte
st.write("Bienvenue dans cette application !")
# Affichage d'un graphique -----------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
st.pyplot(plt)
# Sélecteur de valeurs ---------------------------------------------------------
option = st.selectbox("Choisissez une option", ("Option 1", "Option 2", 
                                                "Option 3"))
st.write("Vous avez sélectionné :", option)
# Barre de progression ---------------------------------------------------------
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
# Affichage des données dans un tableau ----------------------------------------
import pandas as pd
data = pd.DataFrame({
    "Colonne 1": [1, 2, 3, 4],
    "Colonne 2": [10, 20, 30, 40]
})
st.write("Données:", data)
# Affichage d'une carte --------------------------------------------------------
import folium
# Créer une carte Folium
data = {
    'Well Name': ['Paris', 'Londres', 'New York', 'Tokyo'],
    'latitude': [48.8566, 51.5074, 40.7128, 35.6895],
    'longitude': [2.3522, -0.1278, -74.0060, 139.6917]
}
df = pd.DataFrame(data)
st.write("Carte :")
st.map(df)
# Affichage d'une vidéo --------------------------------------------------------
st.write("Vidéo :")
st.video("../ressource/video/video.mp4")
# Affichage d'une image---------------------------------------------------------
st.write("Image :")
st.image("../ressource/image/image.png", caption="Une image")
# Affichage de code ------------------------------------------------------------
code = '''
def hello():
    print("Hello, Streamlit!")

hello()
'''
st.write("Code :")
st.code(code, language='python')
