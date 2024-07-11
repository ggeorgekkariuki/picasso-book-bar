# Get the poster URL
def get_book_details(book_title):
    """Get the ISBN, author and Image URL given an exact title"""
    return final_rating[final_rating['title'] == book_title].sort_values(by='year', ascending=False)\
            .iloc[0,:][['ISBN', 'author', 'img_url']]

# Function to recommend books and returns the poster
def recommend_books(book_name):
    """This function takes a book name and returns other book suggestions"""
    # Obtain the book ID
    book_id = np.where(book_pivot.index == book_name)
    # Obtain the whole record
    record = book_pivot.iloc[book_id, :].values.reshape(1, -1)
    # Distances and suggestions
    distance, suggestion = book_model.kneighbors(record, n_neighbors=6)