import streamlit as st

def books():
    import streamlit as st
    import numpy as np
    from pickles import book_names, author_names
    from functions import recommend_books, recommended_author

    # Webpage Titles
    st.header("Picasso's But For Books")
    st.subheader("A book recommendation system using Machine Learning")

    # Drop Down Button for selecting a book
    selected_books = st.selectbox(label="Please type or select a book", options=book_names)

    # Create a button that returns a recommendation
    if st.button('Show Book Recommendation'):
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

def authors():

    import streamlit as st
    from pickles import author_names
    from functions import recommended_author

    # Drop Down Button for selecting a book
    selected_author = st.selectbox(label="Please type or select an author", options=author_names)

    # Create a button that returns a recommendation
    if st.button('Show Author Recommendation'):
        recommended_author, book_title, poster = recommended_author(selected_author)

        # Define columns for the posters
        col1, col2, col3, col4, col5 = st.columns(5)

        # Render the columns
        with col1:
            st.text(recommended_author[1])# Book Title
            st.text(book_title[1]) # Poster
            st.image(poster[1]) # Poster
        with col2:
            st.text(recommended_author[2])# Book Title
            st.text(book_title[2])
            st.image(poster[2])
        with col3:
            st.text(recommended_author[3])# Book Title
            st.text(book_title[3])
            st.image(poster[3])
        with col4:
            st.text(recommended_author[4])# Book Title
            st.text(book_title[4])
            st.image(poster[4])
        with col5:
            st.text(recommended_author[5])# Book Title
            st.text(book_title[5]) # Poster
            st.image(poster[5])

page_names_to_funcs = {
    # "—": intro,
    "Book Aisle": books,
    "Authors Parade": authors,
    # "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()