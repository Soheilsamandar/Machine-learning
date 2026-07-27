import pandas as pd
from random import randint
import random
data = []


for i in range(1000):

    year = randint(2000, 2025)

    mileage = randint(0, 300000)

    engine = randint(1000, 4000)

    horsepower = randint(70, 500)

    cylinders = random.choice([3, 4, 6, 8])

    owners = randint(0, 5)

    gearbox = random.choice([0, 1])
    # 0 = Manual
    # 1 = Automatic

    price = (
        (year - 1990) * 800
        - mileage * 0.02
        + engine * 15
        + horsepower * 50
        + cylinders * 3000
        - owners * 5000
        + gearbox * 20000
        + randint(-20000, 20000)
    )

    data.append([year, mileage, engine, horsepower, cylinders, owners, gearbox, price])


columns = [
    "Year",
    "Mileage",
    "Engine",
    "Horsepower",
    "Cylinders",
    "Owners",
    "Gearbox",
    "Price",
]


df = pd.DataFrame(data, columns=columns)

file_path = "3.Car Price Prediction\car_price.csv"
df.to_csv(file_path, index=False)


print(df.head())

print("\nDataset Created!")


import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.scatter(df["Horsepower"], df["Price"], alpha=0.6, color="darkorange")
plt.title("Car Price Prediction")
plt.xlabel("Horsepower")
plt.ylabel("Price")
plt.grid(True)
plt.show()
