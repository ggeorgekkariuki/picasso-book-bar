# Picasso Library - But For Books

View the [streamlit app here](https://picaapp-book-bar.streamlit.app/)

### Tools used:

1. StreamLit
2. Pandas
3. Python
4. Matplotlib
5. Seaborn

## What are Recommendation Systems

Recommendation System is an algorithm that can suggest products based on user or item activities.

Types:

- **Content-based** - These systems are based on the characteristics of the items themselves
- **Collaborative Filtering** - These systems use a collection of user ratings of items to make recommendations. Users
  with similar interests will receive recommendations based on previous users viewing.
- **Hybrid** - These systems use the content-based and collaborative filtering to form a more powerful recommendation system.

### Stages of this project

1. Obtain the dataset
2. Analysis
3. Preprocessing of the data
4. Modelling
5. Deployment

### Data Source

The data was sourced from [Kaggle](https://www.kaggle.com/datasets/ra4u12/bookrecommendation)

### Modelling
Using the NearestNeighbors algorithm, a cluster was formed that tagged each book or author to a particular cluster that enabled suggestion of books or authors according to the distance.