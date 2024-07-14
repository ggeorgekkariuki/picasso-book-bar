import streamlit as st

def intro():
    import streamlit as st

    st.header("Picasso's Bar and Lounge")
    st.subheader("Welcome to Picasso's - We love books and love machine learning")
    st.text("Visit our side bar to get fresh recommendations")

    st.write("""
             This project utilises Machine Learning to create a recommendation system using the Collaborative Filtering Recommendation System.

             The data was sourced by from Kaggle - Book Recommendation Competition.

             This was a little fun (3 days of constant frustration) to create
             """)

def books():
    # Imports
    import streamlit as st
    import numpy as np
    from pickles import book_names
    from functions import recommend_books

    # Webpage Titles
    st.header("Picasso's Bar - But For Books")
    st.subheader("A book recommendation system using Machine Learning")

    # Drop Down Button for selecting a book
    selected_books = st.selectbox(label="Please type or select a book", options=book_names)

    # Create a button that returns a recommendation
    if st.button('Show Book Recommendation'):
        recommended_books, posters, authors, ratings = recommend_books(selected_books)

        # Define columns for the posters
        col1, col2, col3, col4, col5 = st.columns(5)

        # Render the columns
        with col1:
            st.text(recommended_books[1])# Book Title
            st.text(authors[1])# Book Title
            st.image(posters[1]) # Poster
            st.write(f"Rated: {ratings[1]}") # Ratings
        with col2:
            st.text(recommended_books[2])
            st.text(authors[2])
            st.image(posters[2])
            st.write(f"Rated: {ratings[2]}") # Ratings
        with col3:
            st.text(recommended_books[3])
            st.text(authors[3])
            st.image(posters[3])
            st.write(f"Rated: {ratings[3]}") # Ratings
        with col4:
            st.text(recommended_books[4])
            st.text(authors[4])
            st.image(posters[4])
            st.write(f"Rated: {ratings[4]}") # Ratings
        with col5:
            st.text(recommended_books[5])
            st.text(authors[5])
            st.image(posters[5])
            st.write(f"Rated: {ratings[5]}") # Ratings

def authors():

    import streamlit as st
    from pickles import author_names
    from functions import recommended_author

    # Webpage Titles
    st.header("Picasso's Lounge - Art is for Artist")
    st.subheader("An Author recommendation system using Machine Learning")

    # Drop Down Button for selecting a book
    selected_author = st.selectbox(label="Please type or select an author", options=author_names)

    # Create a button that returns a recommendation
    if st.button('Show Author Recommendation'):
        recommended_author, book_title, poster, ratings = recommended_author(selected_author)

        # Define columns for the posters
        col1, col2, col3, col4, col5 = st.columns(5)

        # Render the columns
        with col1:
            st.text(book_title[1]) # Title
            st.image(poster[1]) # Poster
            st.write(f"Rated: {ratings[1]}")
        with col2:
            st.text(book_title[2])
            st.image(poster[2])
            st.write(f"Rated: {ratings[2]}")
        with col3:
            st.text(book_title[3])
            st.image(poster[3])
            st.write(f"Rated: {ratings[3]}")
        with col4:
            st.text(book_title[4])
            st.image(poster[4])
            st.write(f"Rated: {ratings[4]}")
        with col5:
            st.text(book_title[5]) 
            st.image(poster[5])
            st.write(f"Rated: {ratings[5]}")

# Pages
page_names_to_funcs = {
    "Home": intro,
    "Book Aisle": books,
    "Authors Parade": authors
}

# Side Bar
st.sidebar.header("Please Select An Item From the selection below.")
demo_name = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()