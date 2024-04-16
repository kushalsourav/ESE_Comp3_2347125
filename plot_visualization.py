import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

def load_data():
    return pd.read_csv("WomensClothingE-CommerceReviews - WomensClothingE-CommerceReviews.csv")



data = load_data();

print(data)

print(data.describe())

print(data.info);

st.title("3D Plot Visualization")

st.header("Plots")

st.sidebar.title("Menus")
selected_columns = st.sidebar.multiselect("Select columns", data.columns)
selected_columns2 = st.sidebar.select_slider("select coulms", data.columns)


average_age= data[selected_columns].median()
rating = data["Rating"].nunique()
st.write(f"Average {selected_columns}: {average_age}")
st.write(f"{selected_columns2} describe: {data[selected_columns2].describe()}")



st.header("Relationship between the Age , Rating and Postive Feedback of the cusomers")
relationship_3d = px.scatter_3d(data, x='Age', y='Rating', z='Positive Feedback Count', color='Rating',
                                    labels={'Age': 'Age', 'Rating': 'Rating', 'Positive Feedback Count': 'Positive Feedback Count'},
                                    title="Relationship between the Age , Rating and Postive Feedback of the cusomers")
st.plotly_chart(relationship_3d)