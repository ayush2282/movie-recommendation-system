from recommender_engine import build_model, recommend

if __name__ == "__main__":
    movies, similarity = build_model()

    movie_name = input("Enter a movie name: ")
    results = recommend(movie_name, movies, similarity)

    print("\n Recommended Movies: ")
    for movie in results:
        print("-" + movie)
