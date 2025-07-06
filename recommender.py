import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
df=pd.read_csv("data/clean_movie.csv")

tfidf=TfidfVectorizer(stop_words="english")
tfidf_matrix=tfidf.fit_transform(df["text"])

knn_model=NearestNeighbors(metric='cosine',algorithm='brute')
knn_model.fit(tfidf_matrix)

def recommend_movies(input_text,top_n=10):
    input_text=input_text.lower()
    input_vector=tfidf.transform([input_text])
    disstances,indices=knn_model.kneighbors(input_vector,n_neighbors=top_n)
    results=[]
    for i in indices.flatten():
        title=df.iloc[i]["clean_title"]
        genre=df.iloc[i]["genres"]
        results.append((title,genre))
    return results

