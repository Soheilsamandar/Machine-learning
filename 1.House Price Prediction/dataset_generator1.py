import pandas as pd
from random import randint

rows = []
for i in range(1000):
    area = randint(50, 3000)
    bedrooms = randint(1, 6)
    bathrooms = randint(1, 4)
    age = randint(0, 30)
    garage = randint(0, 2)
    floor = randint(1, 10)
    distance = randint(1, 25)

    prices = (
        area * 3500
        + bedrooms * 2500
        + bathrooms * 18000
        + garage * 12000
        + floor * 3000
        - age * 1800
        - distance * 5000
        + (randint(-25000, 25000))
    )
    rows.append([area, bedrooms, bathrooms, garage, floor, age, distance, prices])
columns = [
    "Area",
    "Bedrooms",
    "Bathrooms",
    "Age",
    "Garage",
    "Floor",
    "Distance",
    "Price",
]

df = pd.DataFrame(rows, columns=columns)
file_path = "1.House Price Prediction/house_price.csv"
df.to_csv(file_path, index=False)
print(df.head())


import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))
plt.scatter(df["Price"], df["Area"], alpha=0.6, color="royalblue")
plt.title("House Price Prediction")
plt.xlabel("Price")
plt.ylabel("Area")
plt.grid(True)
plt.show()
