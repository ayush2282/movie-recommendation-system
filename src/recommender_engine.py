import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
    # 1. Find index of the movie
    movie_name = movie_name.lower()
    movie_index = movies[movies['title'].str.lower() == movie_name].index

    if len(movie_index) == 0:
        return ["Movie not found! Check spelling."]

    movie_index = movie_index[0]

    # 2. Fetch similarity scores
    distances = similarity[movie_index]

    # 3. Sort and get top 5 recommendations
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
