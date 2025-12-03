from recommender import recommend_movies

if __name__ == "__main__":
    movies = ["Inception", "Interstellar", "The Dark Knight"]
    print("Top Movie Recommendations (Master + Branch 1)")
    for movie, rating in recommend_movies(movies):
        print(f"- {movie} (Rating: {rating}/5)")
