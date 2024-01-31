import streamlit as st
import numpy as np
from make_pred import make_prediction
import json
import pandas as pd
import plotly.express as px
import requests

# Setup data from csv
df = pd.read_csv("iris_data.csv")
# sepal_length,sepal_width,petal_length,petal_width,species

# Setup title page
st.set_page_config(page_title="Prediction")
st.header("Prediction - Iris Dataset")
st.markdown("Utilize the RandomForestClassifier to make predictions for the classification of the species data."
            "The predictions will be displayed on the graphs below to intuitively understand how they were made.")
st.sidebar.header("Make Prediction")

sep_len = st.sidebar.text_input("Sepal Length")
sep_wid = st.sidebar.text_input("Sepal Width")
pet_len = st.sidebar.text_input("Petal Length")
pet_wid = st.sidebar.text_input("Petal Width")
make_pred_API = st.sidebar.button("Predict")

# Affichage de scatterplot
plot1 = px.scatter(
    df,
    x="petal_length",
    y="petal_width",
    title="Petal Length vs Petal Width",
    color="species")

plot2 = px.scatter(
    df,
    x="sepal_length",
    y="petal_length",
    title="Sepal Length vs Petal Length",
    color="species")

# Launch prediction with API
if make_pred_API:
    # Construire l'URL avec les paramètres
    url = f"http://localhost:8000/{float(sep_len)}/{float(sep_wid)}/{float(pet_len)}/{float(pet_wid)}"

    # Envoyer la requête à FastAPI
    response = requests.get(url)

    # Vérifier si la requête a réussi (statut 200)
    if response.status_code == 200:
        species_pred = response.json()["prediction"]
        st.success(f"Prediction result: {species_pred} ")
    else:
        st.error("Error in prediction request.")

    # Transformer mes x1/x2/x3/x4 en df
    p1 = [float(sep_len), float(sep_wid), float(pet_len), float(pet_wid)]
    x = np.array([p1])
    row = {"sepal_length": [float(sep_len)],
           "sepal_width": [float(sep_wid)],
           "petal_length": [float(pet_len)],
           "petal_width": [float(pet_wid)]}

    p1_df = pd.DataFrame(row)

    plot1.add_scatter(x=p1_df["petal_length"], 
                      y=p1_df["petal_width"],
                      mode='markers',  
                      name=species_pred,  
                      marker=dict(
                            color='red',  # Couleur des points
                            size=10,  # Taille des points
                            symbol='circle',  # Type de marqueur (vous pouvez choisir parmi divers symboles)
                            line=dict(
                                color='white',  # Couleur de la bordure des points
                                width=2  # Largeur de la bordure des points
                            )
                      ))
    plot2.add_scatter(x=p1_df["sepal_length"], 
                      y=p1_df["petal_length"],
                      mode='markers',  
                      name=species_pred,  
                      marker=dict(
                            color='red',  # Couleur des points
                            size=10,  # Taille des points
                            symbol='circle',  # Type de marqueur (vous pouvez choisir parmi divers symboles)
                            line=dict(
                                color='white',  # Couleur de la bordure des points
                                width=2  # Largeur de la bordure des points
                            )
    ))

st.plotly_chart(plot1)
st.plotly_chart(plot2)


























# Managing input data
# p1 = ["", "", "", ""]

# plot1 = px.scatter(
#     df,
#     x="petal_length",
#     y="petal_width",
#     title="Petal Length vs Petal Width",
#     color="species")

# plot2 = px.scatter(
#     df,
#     x="sepal_length",
#     y="petal_length",
#     title="Sepal Length vs Petal Length",
#     color="species")

# # Launch prediction with API
# if make_pred_API:
#     # Construire l'URL avec les paramètres
#     url = f"http://localhost:8000/{float(sep_len)}/{float(sep_wid)}/{float(pet_len)}/{float(pet_wid)}"

#     # Envoyer la requête à FastAPI
#     response = requests.get(url)

#     # Vérifier si la requête a réussi (statut 200)
#     if response.status_code == 200:
#         species_pred = response.json()["prediction"]
#         st.success(f"Prediction result: {species_pred}")
#     else:
#         st.error("Error in prediction request.")

#     p1 = [float(sep_len), float(sep_wid), float(pet_len), float(pet_wid)]
#     row = {"sepal_length": [float(sep_len)],
#            "sepal_width": [float(sep_wid)],
#            "petal_length": [float(pet_len)],
#            "petal_width": [float(pet_wid)]}
#     p1_df = pd.DataFrame(row)

#     st.subheader(f"Predicted Species: {species_pred}")
#     plot1.add_scatter(x=p1_df["petal_length"], 
#                       y=p1_df["petal_width"],
#                       mode='markers',  
#                       name=species_pred,  
#                       marker=dict(
#                             color='red',  # Couleur des points
#                             size=10,  # Taille des points
#                             symbol='circle',  # Type de marqueur (vous pouvez choisir parmi divers symboles)
#                             line=dict(
#                                 color='white',  # Couleur de la bordure des points
#                                 width=2  # Largeur de la bordure des points
#                             )
#                       ))
#     plot2.add_scatter(x=p1_df["sepal_length"], 
#                       y=p1_df["petal_length"],
#                       mode='markers',  
#                       name=species_pred,  
#                       marker=dict(
#                             color='red',  # Couleur des points
#                             size=10,  # Taille des points
#                             symbol='circle',  # Type de marqueur (vous pouvez choisir parmi divers symboles)
#                             line=dict(
#                                 color='white',  # Couleur de la bordure des points
#                                 width=2  # Largeur de la bordure des points
#                             )
#     ))

# # Making a prediction and displaying data
# if make_pred:
#     p1 = [float(sep_len), float(sep_wid), float(pet_len), float(pet_wid)]
#     x = np.array([p1])
#     row = {"sepal_length": [float(sep_len)],
#            "sepal_width": [float(sep_wid)],
#            "petal_length": [float(pet_len)],
#            "petal_width": [float(pet_wid)]}

#     p1_df = pd.DataFrame(row)
#     species_pred = make_prediction(x)

#     st.subheader(f"Predicted Species: {species_pred}")
#     plot1.add_scatter(x=p1_df["petal_length"], 
#                       y=p1_df["petal_width"],
#                       mode='markers',  
#                       name=species_pred,  
#                       marker=dict(
#                             color='red',  # Couleur des points
#                             size=10,  # Taille des points
#                             symbol='circle',  # Type de marqueur (vous pouvez choisir parmi divers symboles)
#                             line=dict(
#                                 color='white',  # Couleur de la bordure des points
#                                 width=2  # Largeur de la bordure des points
#                             )
#                       ))
#     plot2.add_scatter(x=p1_df["sepal_length"], 
#                       y=p1_df["petal_length"],
#                       mode='markers',  
#                       name=species_pred,  
#                       marker=dict(
#                             color='red',  # Couleur des points
#                             size=10,  # Taille des points
#                             symbol='circle',  # Type de marqueur (vous pouvez choisir parmi divers symboles)
#                             line=dict(
#                                 color='white',  # Couleur de la bordure des points
#                                 width=2  # Largeur de la bordure des points
#                             )
#     ))

# st.plotly_chart(plot1)
# st.plotly_chart(plot2)

# print('toto4')

# #5.2/2.7/3.9/1.4