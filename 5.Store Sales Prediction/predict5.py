import pandas as pd
import joblib

# Load Trained Model
model = joblib.load("5.Store Sales Prediction\sales_model.pkl")

print("=" * 40)
print("STORE SALES PREDICTION")
print("=" * 40)

customers = int(input("Number of Customers: "))
price = float(input("Product Price: "))
advertising = float(input("Advertising Budget: "))
discount = float(input("Discount (%): "))
stock = int(input("Stock: "))
day = int(input("Day of Week (1-7): "))

new_data = pd.DataFrame(
    {
        "Customers": [customers],
        "Price": [price],
        "Advertising": [advertising],
        "Discount": [discount],
        "Stock": [stock],
        "Day": [day],
    }
)

prediction = model.predict(new_data)

print("\nPredicted Sales:")
print(round(prediction[0], 2))
