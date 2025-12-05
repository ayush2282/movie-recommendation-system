import pandas as pd 

def preprocess_movies(movies):
    # conver genres from string to list
    movies['genres'] = movies['genres'].apply(lambda x: x.split('|'))

    # combine usefull text features for each movie
    movies['tags'] = movies['genres'].apply(lambda x: " ".join(x))

    return movies

if __name__ == "__main__":
    movies = pd.read_csv('data/movies.csv')
    movies = preprocess_movies(movies)
    print(movies[['title', 'tags']].head())