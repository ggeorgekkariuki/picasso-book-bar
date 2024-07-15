from pickles import *
import numpy as np

class BookDetails():
    def __init__(self, book_id=None, name=None):
        if book_id != None and name == None:
            self.book_name = book_pivot.index[book_id]
        else:
            self.book_name = name
            
        self.book_records = final_rating[final_rating['title']==self.book_name]
        
    def fetch_book(self):
        return self.book_name
    
    def fetch_poster(self):
        return self.book_records.iloc[0]['img_url']
    
    def fetch_author(self):
        return self.book_records.iloc[0]['author']
    
    def fetch_mean_ratings(self):
        avg_rating = round(self.book_records.groupby('title')['rating'].mean().values[0], 1)
        return avg_rating

# Function to recommend books
def recommend_books(book_name):
    """This function takes in a name of a book
    and returns other book suggestions"""
    # Obtain the book ID
    book_id = np.where(book_pivot.index == book_name)[0][0]

    # Obtain the whole record
    record = book_pivot.iloc[book_id, :].values.reshape(1, -1)

    # Distances and suggestions
    distance, suggestion = book_model.kneighbors(record, n_neighbors=6)

    # Empty book list to store the books
    book_list, poster_url, authors, ratings= [], [], [], []

    for idx in suggestion[0]:
        book = BookDetails(idx)
        book_list.append(book.fetch_book())
        poster_url.append(book.fetch_poster())
        authors.append(book.fetch_author())
        ratings.append(book.fetch_mean_ratings())

    return book_list, poster_url, authors, ratings

class AuthorsDetails():
    def __init__(self, author_id=None, name=None):
        if author_id != None and name == None:
            self.author_name = author_pivot.index[author_id]
        else:
            self.author_name = name
            
        # Contains all the Authors books in the database    
        self.authors_books = final_rating[final_rating['author']==self.author_name]
        # Group the books by their average ratings in descending order
        self.df = self.authors_books.groupby(['title'])['rating'].mean().sort_values(ascending=False)
        
    def fetch_author(self):
        return self.author_name
    
    def fetch_top_rated(self):
        book_name = self.df.index[np.argmax(self.df)]
        return book_name
    
    def top_books(self):
        """Top 2 books and their posters"""
        books = self.df.iloc[:3]
        book_names = list(books.index)
        book_ratings = [round(rating, 1) for rating in books.values]
        posters = []
        for book in book_names:
            posters.append(final_rating.loc[(final_rating['title'] == book) 
                         & (final_rating['author'] == self.author_name)]['img_url'].iloc[0])
        return book_names, book_ratings, posters
    
    def fetch_mean_rating(self):
        return round(self.df[np.argmax(self.df)], 1)
    
    def fetch_poster(self):
        book_name = self.df.index[np.argmax(self.df)]
        poster = final_rating.loc[(final_rating['title'] == book_name) 
                         & (final_rating['author'] == self.author_name)]['img_url'].iloc[0]
        return poster
    
def recommended_author(author_name):
    """This function takes a booklist of name and returns other book suggestions"""
    # Obtain the book ID
    idx = np.where(author_pivot.index == author_name)[0][0]

    # Obtain the whole record
    record = author_pivot.iloc[idx, :].values.reshape(1, -1)

    # Distances and suggestions
    distance, suggestion = author_model.kneighbors(record, n_neighbors=6)

    # Empty book list to store the books
    authors, top_rated_books, posters, ratings = [], [], [], []

    for idx in suggestion[0]:
        author = AuthorsDetails(idx)
        authors.append(author.fetch_author())
        top_rated_books.append(author.fetch_top_rated())
        posters.append(author.fetch_poster())
        ratings.append(author.fetch_mean_rating())

    return authors, top_rated_books, posters, ratings

def author_more_works(name):
    """Find at least 5 top rated works by an author"""
    author = AuthorsDetails(name=name)
    book, rating, poster = author.top_books()
    return book, rating, poster