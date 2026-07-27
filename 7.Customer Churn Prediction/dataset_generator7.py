import pandas as pd
import random

data = []

for i in range(2000):
    age = random.randint(18, 70)
    gender = random.randint(0, 1)
    years = random.randint(1, 15)
    purchases = random.randint(1, 300)
    support = random.randint(0, 20)
    satisfaction = random.randint(1, 10)
    monthly_bill = random.randint(10, 300)
    score = 0
    if satisfaction >= 6:
        score += 2
    if years >= 3:
        score += 2
    if purchases >= 50:
        score += 2
    if support <= 5:
        score += 2
    if monthly_bill < 150:
        score += 1
    churn = 0
    if score < 5:
        churn = 1
    data.append(
        [age, gender, years, purchases, support, satisfaction, monthly_bill, churn])

columns = [
    "Age",
    "Gender",
    "Years",
    "Purchases",
    "SupportTickets",
    "Satisfaction",
    "MonthlyBill",
    "Churn",
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("7.Customer Churn Prediction\customer_churn.csv", index=False)

print(df.head())

import matplotlib.pyplot as plt
churn = df[df["Churn"] == 1]
not_churn = df[df["Churn"] == 0]
plt.figure(figsize=(8, 6))
plt.scatter(
    not_churn["Years"],
    not_churn["Satisfaction"],
    color="green",
    label="Stayed",
    alpha=0.7,
)
plt.scatter(
    churn["Years"], churn["Satisfaction"], color="red", label="Churn", alpha=0.7
)
plt.title("Customer Churn Dataset")
plt.xlabel("Years as Customer")
plt.ylabel("Satisfaction")
plt.legend()
plt.grid(True)
plt.show()
