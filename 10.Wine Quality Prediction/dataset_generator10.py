import pandas as pd
import random

data = []


for i in range(2000):
    alcohol = round(random.uniform(8, 15), 2)
    sugar = round(random.uniform(0.5, 10), 2)
    acidity = round(random.uniform(3, 9), 2)
    density = round(random.uniform(0.990, 1.005), 4)
    ph = round(random.uniform(2.8, 4.0), 2)
    sulphates = round(random.uniform(0.3, 1.5), 2)
    quality_score = 0
    if alcohol > 12:
        quality_score += 2
    if sugar < 4:
        quality_score += 1
    if acidity > 5:
        quality_score += 1
    if sulphates > 0.8:
        quality_score += 1
    if ph > 3:
        quality_score += 1
    quality = 3 + quality_score + random.randint(-1, 1)
    if quality < 3:
        quality = 3
    if quality > 10:
        quality = 10
    data.append([alcohol, sugar, acidity, density, ph, sulphates, quality])
columns = ["Alcohol", "Sugar", "Acidity", "Density", "pH", "Sulphates", "Quality"]
df = pd.DataFrame(data, columns=columns)
df.to_csv("10.Wine Quality Prediction\wine_quality.csv", index=False)
print(df.head())
print("Dataset Created")

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.scatter(df["Alcohol"], df["Quality"], alpha=0.6, color="firebrick")
plt.title("Wine Quality Prediction")
plt.xlabel("Alcohol")
plt.ylabel("Quality")
plt.grid(True)
plt.show()
