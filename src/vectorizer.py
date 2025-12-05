import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def vectorize_tags(movies):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies["tags"]).toarray()
    return vectors, cv

if __name__ == "__main__":
    movies = pd.read_csv("data/movies.csv")

    # 1. genres -> list
    movies["genres"] = movies["genres"].apply(lambda x: x.split("|"))

    # 2. list -> string
    movies["tags"] = movies["genres"].apply(lambda x: " ".join(x))

    # 3. ADD TITLES into tags (NEW)
    movies["tags"] = movies["title"] + " " + movies["tags"]

    # debug prints
    print(movies["tags"].head())

    vectors, cv = vectorize_tags(movies)
    print("Vectors shape:", vectors.shape)
    print("Vocabulary size:", len(cv.get_feature_names_out()))
