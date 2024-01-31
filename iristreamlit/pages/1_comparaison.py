import streamlit as st
import pandas as pd
import plotly.express as px

# Setup data
df = pd.read_csv("iris_data.csv")
# columns name: sepal_length,sepal_width,petal_length,petal_width,species

# Make page
st.set_page_config(page_title="Iris Dataset")
st.header("Comparison - Iris Dataset")
st.markdown("Explore the variables to understand their relationships and how they correlate with the species. "
            "As patterns emerge, we can intuitively understand how the RandomForestClassifier makes decisions in classifying data.")
st.sidebar.header("Variable Comparison")

# Setting graph to display
options = st.sidebar.radio("Select comparison",
                           options=["Sepal Length Vs Sepal Width",
                                    "Petal Length Vs Petal Width",
                                    "Sepal Length Vs Petal Width",
                                    "Sepal Width Vs Petal Length"])

if options == "Sepal Length Vs Sepal Width":
    plot = px.scatter(
        (df),
        x="sepal_length",
        y="sepal_width",
        color="species",
        title=options)
    # Personnalisation des axes
    plot.update_xaxes(title_text="Sepal Length")
    plot.update_yaxes(title_text="Sepal Width")

elif options == "Petal Length Vs Petal Width":
    plot = px.scatter(
        (df),
        x="petal_length",
        y="petal_width",
        color="species",
        title=options)
    # Personnalisation des axes
    plot.update_xaxes(title_text="Petal Length")
    plot.update_yaxes(title_text="Petal Width")

elif options == "Sepal Length Vs Petal Width":
    plot = px.scatter(
        (df),
        x="sepal_length",
        y="petal_width",
        color="species",
        title=options)
    # Personnalisation des axes
    plot.update_xaxes(title_text="Sepal Length")
    plot.update_yaxes(title_text="Petal Width")

elif options == "Sepal Width Vs Petal Length":
    plot = px.scatter(
        (df),
        x="sepal_width",
        y="petal_length",
        color="species",
        title=options)
    # Personnalisation des axes
    plot.update_xaxes(title_text="Sepal Width")
    plot.update_yaxes(title_text="Petal Length")

st.plotly_chart(plot)