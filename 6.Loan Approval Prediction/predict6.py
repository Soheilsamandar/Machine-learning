import pandas as pd
import joblib

model = joblib.load("6.Loan Approval Prediction\loan_model.pkl")

print("Loan Approval Prediction")

age = int(input("Age: "))
income = int(input("Income: "))
credit = int(input("Credit Score: "))
loan = int(input("Loan Amount: "))
employment = int(input("Employment Years: "))
married = int(input("Married (0/1): "))
existing = int(input("Existing Loans: "))

new_customer = pd.DataFrame(
    {
        "Age": [age],
        "Income": [income],
        "CreditScore": [credit],
        "LoanAmount": [loan],
        "EmploymentYears": [employment],
        "Married": [married],
        "ExistingLoans": [existing],
    }
)

prediction = model.predict(new_customer)

if prediction[0] == 1:

    print("\nLoan Approved")

else:

    print("\nLoan Rejected")
