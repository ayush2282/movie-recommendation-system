from recommender import recommend_movies

if __name__ == "__main__":
    movies = ["Inception", "Interstellar", "The Dark Knight"]
    print("Recommended Movies:")
    for movie in recommend_movies(movies):
        print("-", movie)
