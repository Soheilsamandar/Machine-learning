import pandas as pd
import joblib

model = joblib.load("11.Movie Recommendation System\movie_model.pkl")


matrix = joblib.load("11.Movie Recommendation System\movie_matrix.pkl")


print("Movie Recommendation System")

print("---------------------------")


user = int(input("Enter User ID: "))


if user not in matrix.index:

    print("User Not Found")

    exit()


user_data = matrix.loc[user].values.reshape(1, -1)


distance, indices = model.kneighbors(user_data, n_neighbors=5)


print("\nRecommended Users:")


for index in indices[0]:

    print(matrix.index[index])
