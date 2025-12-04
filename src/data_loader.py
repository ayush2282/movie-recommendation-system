import pandas as pd 

def load_data():
    movies = pd.read_csv('data/movies.csv')
    ratings = pd.read_csv('data/ratings.csv')
    return movies, ratings

if __name__ == "__main__":
    m, r = load_data()
    print("Movies :", m.shape)
    print("Ratings :", r.shape)
    