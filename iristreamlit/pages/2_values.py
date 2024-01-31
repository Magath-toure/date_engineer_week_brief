import streamlit as st
import pandas as pd
import plotly.express as px

# Setup data
df = pd.read_csv("iris_data.csv")
# sepal_length,sepal_width,petal_length,petal_width,species

# Make page
st.set_page_config(page_title="Iris Dataset")
st.header("Values - Iris Dataset")
st.markdown("Explore the relationship between each individual variable and each species. "
            "We can intuit patterns within the individual values and gain an understanding of how the data is utilized for classification.")
st.sidebar.header("Individual Values")

# Setting graph to display
options = st.sidebar.radio("Select values",
                           options=["sepal_length", "sepal_width", "petal_length", "petal_width"])

show_df = df.filter(items=[options, "species"])

plot1 = px.histogram(
    show_df,
    x=show_df[options],
    title=f"{options} Histogram",
    nbins=30,
    color="species")

st.plotly_chart(plot1)