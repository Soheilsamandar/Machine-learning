import pandas as pd
import joblib

model = joblib.load("4.Employee Salary Prediction\salary_model.pkl")


print("Employee Salary Prediction")

print("--------------------------")


age = int(input("Age: "))


experience = int(input("Experience Years: "))


education = int(input("Education (1 Bachelor / 2 Master / 3 PhD): "))


skills = int(input("Skill Level (1-10): "))


working_hours = int(input("Working Hours Per Week: "))


department = int(input("Department (1 Eng / 2 Manager / 3 Marketing / 4 IT): "))


employee = pd.DataFrame(
    {
        "Age": [age],
        "Experience": [experience],
        "Education": [education],
        "Skills": [skills],
        "Working_Hours": [working_hours],
        "Department": [department],
    }
)


salary = model.predict(employee)


print("\nPredicted Salary:")

print(round(salary[0], 2))
