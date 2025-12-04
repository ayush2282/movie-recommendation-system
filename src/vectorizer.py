import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def vectorize_tags(movies):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies["tags"]).toarray()
    return vectors, cv

if __name__ == "__main__":
    movies = pd.read_csv("data/movies.csv")

    # FIX: genres should be split first
    movies["genres"] = movies["genres"].apply(lambda x: x.split("|"))

    # FIX: tags should join the list
    movies["tags"] = movies["genres"].apply(lambda x: " ".join(x))

    vectors, cv = vectorize_tags(movies)
    print("Vectors shape:", vectors.shape)


