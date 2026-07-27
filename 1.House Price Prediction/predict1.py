import pandas as pd
import joblib

model = joblib.load("1.House Price Prediction/house_model.pkl")

print("House Price Prediction")
print("----------------------")

area = float(input("Area (m) :"))
bedrooms = int(input("Bedrooms :"))
bathrooms = int(input("Bathrooms"))
age = int(input("Age :"))
garage = int(input("Garage :"))
floor = int(input("Floor :"))
distance = float(input("Distance from city centers (km) :"))

house = pd.DataFrame({
    "Area":[area],
    "Bedrooms":[bedrooms],
    "Bathrooms":[bathrooms],
    "Age":[age],
    "Garage":[garage],
    "Floor":[floor],
    "Distance":[distance]
})

price = model.predict(house)
print(f"best model predict is : {round(price[0],2)}")