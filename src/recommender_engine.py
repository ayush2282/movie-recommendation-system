import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

def build_model():
    movies = pd.read_csv("data/movies.csv")

    # 1. Preprocessing
    movies["genres"] = movies["genres"].apply(lambda x: x.split("|"))
    movies["tags"] = movies["genres"].apply(lambda x: " ".join(x))
    movies["tags"] = movies["title"] + " " + movies["tags"]

    # 2. Vectorization
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies["tags"]).toarray()

    # 3. Cosine similarity
    similarity = cosine_similarity(vectors)

    return movies, similarity


def recommend(movie_name, movies, similarity):

    # find closest match
    movie_name = movie_name.lower()
    titles = movies['title'].str.lower().tolist()
    close_matches = get_close_matches(movie_name, titles, n=1, cutoff=0.6)

    if not close_matches:
        return ["Movie not found! Try another name."]

    # get the best match
    best_match = close_matches[0]
    movie_index = movies[movies['title'].str.lower() == best_match].index[0]

    # similarity scores
    distances = similarity[movie_index]

    # top 5 recommendations
    movies_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended = []

    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)

    return recommended


if __name__ == "__main__":
    movies, similarity = build_model()
    print(recommend("Toy Story (1995)", movies, similarity))
