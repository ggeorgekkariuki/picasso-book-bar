import streamlit as st
import numpy as np
from pickles import book_names
from functions import recommend_books

# Webpage Titles
st.header("Picasso's But For Books")
st.subheader("A book recommendation system using Machine Learning")

# Drop Down Button for selecting a book
selected_books = st.selectbox(label="Please type or select a book", options=book_names)

# Create a button that returns a recommendation
if st.button('Show Recommendation'):
    recommended_books, posters = recommend_books(selected_books)

    # Define columns for the posters
    col1, col2, col3, col4, col5 = st.columns(5)

    # Render the columns
    with col1:
        st.text(recommended_books[1])# Book Title
        st.image(posters[1]) # Poster
    with col2:
        st.text(recommended_books[2])# Book Title
        st.image(posters[2])
    with col3:
        st.text(recommended_books[3])# Book Title
        st.image(posters[3])
    with col4:
        st.text(recommended_books[4])# Book Title
        st.image(posters[4])
    with col5:
        st.text(recommended_books[5])# Book Title
        st.image(posters[5])