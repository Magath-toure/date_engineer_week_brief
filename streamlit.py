# Importation de la bibliothèque
import streamlit as st
# Titre de l'application
st.title("Ma Première Application Streamlit")

# Sous-titre
st.subheader("Bienvenue sur cette première page !")

# Texte explicatif
st.write("C'est une application simple créée avec Streamlit.")

# Affichage d'une image
st.image("https://example.com/your-image.jpg", caption="Une image cool", use_column_width=True)

# Ajouter un graphique (exemple avec un graphique à barres aléatoire)
import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(10, 1)
st.bar_chart(data)

# Ajouter un widget interactif (exemple avec un curseur)
user_input = st.slider("Sélectionnez une valeur", 0, 100, 50)
st.write(f"Vous avez sélectionné : {user_input}")

# Exécutez l'application avec la commande suivante dans une cellule Jupyter Notebook
# !streamlit run my_app.py