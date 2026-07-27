import pandas as pd
import joblib

model = joblib.load("10.Wine Quality Prediction\wine_model.pkl")


print("Wine Quality Prediction")

print("------------------------")


alcohol = float(input("Alcohol: "))


sugar = float(input("Sugar: "))


acidity = float(input("Acidity: "))


density = float(input("Density: "))


ph = float(input("pH: "))


sulphates = float(input("Sulphates: "))


wine = pd.DataFrame(
    {
        "Alcohol": [alcohol],
        "Sugar": [sugar],
        "Acidity": [acidity],
        "Density": [density],
        "pH": [ph],
        "Sulphates": [sulphates],
    }
)


quality = model.predict(wine)


print("\nPredicted Quality:")

print(round(quality[0], 2))
