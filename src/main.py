from recommender import recommend_movies

if __name__ == "__main__":
    movies = ["Inception", "Interstellar", "The Dark Knight"]
    print("Recommended Movies (Master Version):")
    for movie, rating in recommend_movies(movies):
        print(f"- {movie} (Rating: {rating}/5)")

