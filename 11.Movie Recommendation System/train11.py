import pandas as pd
import joblib


from sklearn.neighbors import NearestNeighbors


from sklearn.preprocessing import StandardScaler

df = pd.read_csv("11.Movie Recommendation System\movies_rating.csv")


matrix = df.pivot_table(index="User", columns="Movie", values="Rating")


matrix = matrix.fillna(0)


scaler = StandardScaler()


scaled = scaler.fit_transform(matrix)


model = NearestNeighbors(metric="cosine", algorithm="brute")


model.fit(scaled)


joblib.dump(model, "11.Movie Recommendation System\movie_model.pkl")


joblib.dump(matrix, "11.Movie Recommendation System\movie_matrix.pkl")


print("Movie Recommendation Model Saved")
