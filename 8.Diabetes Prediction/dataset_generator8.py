import pandas as pd
import random

data = []

for i in range(2000):

    pregnancies = random.randint(0, 10)

    glucose = random.randint(70, 220)

    blood_pressure = random.randint(50, 120)

    skin_thickness = random.randint(10, 60)

    insulin = random.randint(15, 300)

    bmi = round(random.uniform(18, 45), 1)

    age = random.randint(18, 80)

    score = 0

    if glucose > 125:
        score += 2

    if bmi > 30:
        score += 2

    if age > 45:
        score += 1

    if insulin > 180:
        score += 1

    if pregnancies > 4:
        score += 1

    if blood_pressure > 90:
        score += 1

    diabetes = 1 if score >= 5 else 0

    data.append(
        [
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            age,
            diabetes,
        ]
    )

columns = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "Age",
    "Diabetes",
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("8.Diabetes Prediction\diabetes_dataset.csv", index=False)

print(df.head())

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.scatter(df["Glucose"], df["Diabetes"], c=df["Diabetes"], cmap="coolwarm", alpha=0.7)
plt.title("Diabetes Prediction")
plt.xlabel("Glucose")
plt.ylabel("Diabetes")
plt.yticks([0, 1], ["Healthy", "Diabetes"])
plt.grid(True)
plt.show()
