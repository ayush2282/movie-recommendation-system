# 🎬 Movie Recommendation System (Content-Based)

A machine learning project that recommends similar movies using:

- Pandas for data handling  
- CountVectorizer for feature extraction  
- Cosine Similarity for recommendations  
- Fuzzy Matching for flexible user search  
- Clean Git branching workflow  

## 🚀 Features
- Search any movie (even misspelled names)
- Returns top 5 similar movies
- Uses MovieLens dataset
- Modular and scalable ML architecture

## 🧠 How it Works
1. Load movie metadata  
2. Preprocess genres  
3. Create text “tags”  
4. Convert tags → vectors  
5. Build similarity matrix  
6. Recommend top similar movies  

## 📊 Example Output
Enter a movie name: interstellar

 Recommended Movies: 
-Transcendence (2014)
-Divergent (2014)
-I, Frankenstein (2014)
-RoboCop (2014)
-Godzilla (2014)


## 🏗 Project Structure
movie-recommendation-git/  
├── data/. 
│ ├── movies.csv  
│ └── ratings.csv  
├── src/  
│ ├── main.py  
│ ├── data_loader.py  
│ ├── preprocess.py  
│ ├── vectorizer.py  
│ ├── similarity.py  
│ └── recommender_engine.py  
└── README.md  