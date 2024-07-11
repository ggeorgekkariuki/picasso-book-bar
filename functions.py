from pickles import *
from pickles import *
import numpy as np

class BookDetails():
    def __init__(self, book_idx):
        self.book_idx = book_idx
        self.df_idx = np.where(final_rating['title'] == book_pivot.index[self.book_idx])[0][0]

    def fetch_book(self):
        # Find the location of the book in the main df
        # Book
        return book_pivot.index[self.book_idx]

    def fetch_poster(self):
        # URLs
        return final_rating.iloc[self.df_idx]['img_url']

    def fetch_author(self):
        # URLs
        return final_rating.iloc[self.df_idx]['author']


def fetch_poster(suggestion):
    """Obtains the poster for the book"""
    poster_urls = []
    for idx in suggestion[0]:
        book = BookDetails(book_idx=idx)
        return poster_urls.append(book.fetch_poster())



# Function to recommend books and returns the poster
def recommend_books(book_name):
    """This function takes a booklist of name and returns other book suggestions"""
    # Obtain the book ID
    book_id = np.where(book_pivot.index == book_name)

    # Obtain the whole record
    record = book_pivot.iloc[book_id, :].values.reshape(1, -1)

    # Distances and suggestions
    distance, suggestion = book_model.kneighbors(record, n_neighbors=6)

    # Empty book list to store the books
    book_list = []

    for i in range(len(suggestion)):
        book_names = book_pivot.index[suggestion[i]]
        for j in book_names:
            book_list.append(j)

    return book_list, poster