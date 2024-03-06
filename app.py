# -*- coding: utf-8 -*-
import streamlit as st
import pickle
import pandas as pd
import requests

# Set Streamlit page configuration
st.set_page_config(
    page_title="Book Recommendation System",
    page_icon="📚",
    layout="wide",
)

# Load data and models
matrix = pickle.load(open("books.pk1", "rb"))
model = pickle.load(open("model.pk1", "rb"))
result = pickle.load(open("result.pk1", "rb"))

# Function to recommend books
def recommend(books):
    recommended_book_names = []
    distances, indices = model.kneighbors(
        matrix.loc[books].values.reshape(1, -1), n_neighbors=11
    )
    st.write("\nRecommended books:\n")
    for i in range(0, len(distances.flatten())):
        if i > 0:
            recommended_book_names.append(matrix.index[indices.flatten()[i]])
    return recommended_book_names

# Apply background color using CSS
st.markdown(
    """
    <style>
        body {
            background-color: #f1f1f1;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit layout
st.title("Book Recommendation System")

# User selection
user_list = result["User-ID"].values
User_ID_book = st.selectbox("Select a user from the drop-down", user_list)
selected_user_id = result[result["User-ID"] == User_ID_book].sort_values(
    "Book-Rating", ascending=False
).head(1)
selected_book = selected_user_id["Book-Title"].values

# Display user selection
st.write("You selected:", User_ID_book)

# Show recommendation on button click
if st.button("Show Recommended Books"):
    recommended_books = recommend(selected_book)
    st.write("Recommended Books:")
    for book in recommended_books:
        st.success(book)




   