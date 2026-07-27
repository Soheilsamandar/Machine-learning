import pandas as pd
import random

data = []


classes = [0, 1, 2]  # Setosa  # Versicolor  # Virginica


for i in range(600):

    flower = random.choice(classes)

    if flower == 0:

        sepal_length = round(random.uniform(4.5, 5.8), 2)
        sepal_width = round(random.uniform(3.0, 4.2), 2)
        petal_length = round(random.uniform(1.0, 1.9), 2)
        petal_width = round(random.uniform(0.1, 0.6), 2)

    elif flower == 1:

        sepal_length = round(random.uniform(5.5, 7.0), 2)
        sepal_width = round(random.uniform(2.0, 3.5), 2)
        petal_length = round(random.uniform(3.0, 5.0), 2)
        petal_width = round(random.uniform(0.8, 1.8), 2)

    else:

        sepal_length = round(random.uniform(6.0, 8.0), 2)
        sepal_width = round(random.uniform(2.5, 3.8), 2)
        petal_length = round(random.uniform(5.0, 7.0), 2)
        petal_width = round(random.uniform(1.5, 2.8), 2)

    data.append([sepal_length, sepal_width, petal_length, petal_width, flower])


columns = ["SepalLength", "SepalWidth", "PetalLength", "PetalWidth", "Species"]


df = pd.DataFrame(data, columns=columns)


df.to_csv("9.Iris Flower Classification\iris_dataset.csv", index=False)


print(df.head())

print("Dataset Created")


import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.scatter(df["PetalLength"], df["PetalWidth"], c=df["Species"])
plt.title("Student Performance Dataset")
plt.xlabel("Study_Hours")
plt.ylabel("Result")
plt.grid(True)
plt.show()
