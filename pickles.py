import pickle

# Load book models
book_model = pickle.load(open('models/book_model.pkl', 'rb'))
author_model = pickle.load(open('models/author_model.pkl', 'rb'))

# Author and Book Names
book_names = pickle.load(open('models/book_names.pkl', 'rb'))
author_names = pickle.load(open('models/author_names.pkl', 'rb'))

# Pivots
book_pivot = pickle.load(open('models/book_pivot.pkl', 'rb'))
author_pivot = pickle.load(open('models/author_pivot.pkl', 'rb'))

# Main DataFrame
final_rating = pickle.load(open('models/final_rating.pkl', 'rb'))