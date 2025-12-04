import pandas as pd 

def preprocess_movies(movies):
    # split genres into a list
    movies['genres'] = movies['genres'].apply(lambda x: x.split('|'))
    return movies

if __name__ == "__main__":
    movies = pd.read_csv('data/movies.csv')
    movies = preprocess_movies(movies)
    print(movies.head())
    