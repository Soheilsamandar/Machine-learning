import pandas as pd
import joblib

model = joblib.load(r"3.Car Price Prediction\car_price_model.pkl")


print("Car Price Prediction")
print("--------------------")


year = int(input("Car Year: "))


mileage = int(input("Mileage: "))


engine = int(input("Engine Size: "))


horsepower = int(input("Horsepower: "))


cylinders = int(input("Cylinders: "))


owners = int(input("Previous Owners: "))


gearbox = int(input("Gearbox (0 Manual / 1 Automatic): "))


car = pd.DataFrame(
    {
        "Year": [year],
        "Mileage": [mileage],
        "Engine": [engine],
        "Horsepower": [horsepower],
        "Cylinders": [cylinders],
        "Owners": [owners],
        "Gearbox": [gearbox],
    }
)


price = model.predict(car)
print("\nPredicted Price:")
print(round(price[0], 2))
