import pandas as pd
import random

users = range(1, 101)

movies = [
    "Interstellar",
    "Inception",
    "Titanic",
    "Avatar",
    "Joker",
    "Matrix",
    "Avengers",
    "Batman",
    "Toy Story",
    "Frozen",
]


data = []


for user in users:

    for movie in movies:

        rating = random.randint(1, 5)

        if random.random() < 0.2:

            rating = 0

        data.append([user, movie, rating])


df = pd.DataFrame(data, columns=["User", "Movie", "Rating"])


df = df[df["Rating"] != 0]


df.to_csv("11.Movie Recommendation System\movies_rating.csv", index=False)


print(df.head())

print("Dataset Created")

import matplotlib.pyplot as plt
pivot = df.pivot(index="User", columns="Movie", values="Rating")
plt.figure(figsize=(12, 8))
plt.imshow(pivot, aspect="auto", cmap="viridis")
plt.colorbar(label="Rating")
plt.title("Movie Ratings Matrix")
plt.xlabel("Movies")
plt.ylabel("Users")
plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=45)
plt.yticks(range(0, len(pivot.index), 10))
plt.tight_layout()
plt.show()
