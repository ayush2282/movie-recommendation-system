import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def create_similarity_matrix(movies):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()
    similarity = cosine_similarity(vectors)
    return similarity

if __name__ == "__main__":
    movies = pd.read_csv('data/movies.csv')
    movies['genres'] = movies['genres'].apply(lambda x: x.split('|'))
    movies['tags'] = movies['genres'].apply(lambda x: ' '.join(x))
    movies['tags'] = movies['title'] + ' ' + movies['tags']

    similarity = create_similarity_matrix(movies)
    print("Similarity matrix shape:", similarity.shape)

