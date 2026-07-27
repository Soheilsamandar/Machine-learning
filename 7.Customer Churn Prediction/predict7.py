import pandas as pd
import joblib

model = joblib.load("7.Customer Churn Prediction\customer_model.pkl")

age = int(input("Age: "))
gender = int(input("Gender (0 Female /1 Male): "))
years = int(input("Years As Customer: "))
purchases = int(input("Purchases: "))
support = int(input("Support Tickets: "))
satisfaction = int(input("Satisfaction (1-10): "))
bill = int(input("Monthly Bill: "))

customer = pd.DataFrame(
    {
        "Age": [age],
        "Gender": [gender],
        "Years": [years],
        "Purchases": [purchases],
        "SupportTickets": [support],
        "Satisfaction": [satisfaction],
        "MonthlyBill": [bill],
    }
)

result = model.predict(customer)

if result[0] == 1:
    print("Customer Will Leave")
else:
    print("Customer Will Stay")
