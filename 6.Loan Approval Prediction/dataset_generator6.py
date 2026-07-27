import pandas as pd
import random

data = []

for i in range(2000):

    age = random.randint(18, 65)
    income = random.randint(15000, 120000)
    credit_score = random.randint(300, 850)
    loan_amount = random.randint(5000, 80000)
    employment = random.randint(0, 35)
    married = random.randint(0, 1)
    existing_loans = random.randint(0, 5)
    score = 0
    if income > 40000:
        score += 1
    if credit_score > 650:
        score += 1
    if employment > 3:
        score += 1
    if existing_loans < 2:
        score += 1
    if loan_amount < income * 0.7:
        score += 1
    if score >= 4:
        status = 1
    else:
        status = 0
    data.append(
        [
            age,
            income,
            credit_score,
            loan_amount,
            employment,
            married,
            existing_loans,
            status,
        ]
    )


columns = [
    "Age",
    "Income",
    "CreditScore",
    "LoanAmount",
    "EmploymentYears",
    "Married",
    "ExistingLoans",
    "LoanStatus",
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("6.Loan Approval Prediction\loan_dataset.csv", index=False)

print(df.head())
print("Dataset Created Successfully")


import matplotlib.pyplot as plt
approved = df[df["LoanStatus"] == 1]
rejected = df[df["LoanStatus"] == 0]
plt.figure(figsize=(8, 6))
plt.scatter(
    approved["Income"],
    approved["CreditScore"],
    color="blue",
    label="Approved",
    alpha=0.7,
)
plt.scatter(
    rejected["Income"],
    rejected["CreditScore"],
    color="red",
    label="Rejected",
    alpha=0.7,
)
plt.title("Loan Approval Dataset")
plt.xlabel("Income")
plt.ylabel("Credit Score")
plt.legend()
plt.grid(True)
plt.show()
