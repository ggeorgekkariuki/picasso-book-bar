from pickles import *
import numpy as np

class BookDetails():
    def __init__(self, book_idx=None, name=None):
        self.book_idx = book_idx
        self.name = name

        if name == None:
            self.df_idx = np.where(final_rating['title'] == book_pivot.index[self.book_idx])[0][0]
        else:
            self.df_idx = np.where(final_rating['title'] == self.name)[0][0]

    def fetch_book(self):
        # Find the location of the book in the main df
        # Book
        if self.name:
            return self.name
        return book_pivot.index[self.book_idx]

    def fetch_poster(self):
        # URLs
        return final_rating.iloc[self.df_idx]['img_url']

    def fetch_author(self):
        # URLs
        return final_rating.iloc[self.df_idx]['author']

# Function to recommend books
def recommend_books(book_name):
    """This function takes in a book title and returns a list of books, poster_urls and authors"""
    # Obtain the book ID
    book_id = np.where(book_pivot.index == book_name)[0][0]

    # Obtain the whole record
    record = book_pivot.iloc[book_id, :].values.reshape(1, -1)

    # Distances and suggestions
    distance, suggestion = book_model.kneighbors(record, n_neighbors=6)

    # Empty book list to store the books
    book_list, poster_url = [], []

    for idx in suggestion[0]:
        book = BookDetails(idx)
        book_list.append(book.fetch_book())
        poster_url.append(book.fetch_poster())

    return book_list, poster_url

class AuthorsDetails():
    def __init__(self, author_id, author='None'):
        self.author_id = author_id

        if author == 'None':
            self.author = author_pivot.index[self.author_id]

    def fetch_author(self):
        # Return the name of the author
        return self.author

    def fetch_top_rated(self):
        # Top Rated Books
        books = []
        for book in final_rating[final_rating['author'] == self.author]\
                .sort_values(by='rating', ascending=False)['title']\
                .unique()[:5]:
            books.append(book)
        return books
    
def recommended_author(author_name):
    """This function takes an authors name and returns other book suggestions"""
    # Obtain the book ID
    idx = np.where(author_pivot.index == author_name)[0][0]

    # Obtain the whole record
    record = author_pivot.iloc[idx, :].values.reshape(1, -1)

    # Distances and suggestions
    distance, suggestion = author_model.kneighbors(record, n_neighbors=6)

    # Empty book list to store the books
    authors, top_rated = [], []

    for idx in suggestion[0]:
        book = AuthorsDetails(idx)
        authors.append(book.fetch_author())
        top_rated.append(book.fetch_top_rated())

    return authors, top_rated