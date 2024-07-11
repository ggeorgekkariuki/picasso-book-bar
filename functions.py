from pickles import *

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