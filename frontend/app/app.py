import streamlit as st
from PIL import Image
from roboflow import Roboflow
import tempfile
import os
import io
import numpy as np

print(os.getcwd())
# Initialiser Roboflow avec votre clé API
rf = Roboflow(api_key="2TxsYnXVroUFJ6qR4qzg")
# Obtenir le modèle souhaité à partir de votre projet Roboflow
project = rf.workspace().project("ipd-pothole-detection")
model = project.version(6).model
# Titre de la page
st.title("Prédiction d'images avec Roboflow")
# Section pour télécharger l'image
st.subheader("Télécharger une image")
uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "jpeg", "png"])
# Vérifier si une image a été téléchargée
if uploaded_file is not None:
    # Charger l'image avec PIL
    image = Image.open(uploaded_file)
    # Redimensionner l'image en 640x640 pixels
    resized_image = image.resize((image.width // 2, image.height // 2))
    # Afficher l'image téléchargée
    st.image(resized_image, caption="Image téléchargée", use_column_width=True)
    # Bouton pour effectuer la prédiction
    if st.button("Prédire"):
        # Enregistrer l'image redimensionnée temporairement sur le disque
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_image:
            image.save(temp_image.name)
        # Effectuer la prédiction avec Roboflow
        path_save = "prediction.jpg"
        pred = model.predict(temp_image.name, confidence=40, overlap=30)
        # prediction = model.predict(temp_image.name, confidence=50, overlap=50).json()
        # Supprimer le fichier temporaire
        os.remove(temp_image.name)
        # # Afficher les résultats de prédiction
        st.subheader("Résultats de prédiction")
        st.json(pred.json())
        # Affiché l'image prédite
        # Créer une nouvelle image à partir du tableau Numpy
        # path_save = "prediction.jpg"
        pred.save(path_save)
        #image = Image.open(path_save)
        # image_array = np.array(image)
        # output_image = Image.fromarray(image_array)

        # # Convertir l'image en bytes
        # output_bytes = io.BytesIO()
        # output_image.save(output_bytes, format="JPEG")

        # # Afficher l'image prédite
        # st.subheader("Image prédite")
        # st.image(output_bytes, caption="Image prédite", use_column_width=True)
        # # path_save = "prediction.jpg"
        # # pred.save(path_save)
        st.image(path_save, caption="Image prédite", use_column_width=True)
