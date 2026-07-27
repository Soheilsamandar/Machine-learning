import pandas as pd
import random

data = []


for i in range(1000):

    age = random.randint(20, 60)

    experience = random.randint(0, 35)

    education = random.choice([1, 2, 3])
    # 1 = Bachelor
    # 2 = Master
    # 3 = PhD

    skills = random.randint(1, 10)

    working_hours = random.randint(20, 60)

    department = random.choice([1, 2, 3, 4])
    # 1 Engineering
    # 2 Management
    # 3 Marketing
    # 4 IT

    salary = (
        20000
        + experience * 1500
        + education * 10000
        + skills * 3000
        + working_hours * 300
        + department * 5000
        + random.randint(-10000, 10000)
    )

    data.append([age, experience, education, skills, working_hours, department, salary])


columns = [
    "Age",
    "Experience",
    "Education",
    "Skills",
    "Working_Hours",
    "Department",
    "Salary",
]


df = pd.DataFrame(data, columns=columns)


df.to_csv(r"4.Employee Salary Prediction\employee_salary.csv", index=False)


print(df.head())

print("\nDataset Created Successfully!")


import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.scatter(df["Experience"], df["Salary"], alpha=0.6, color="green")
plt.title("Employee Salary Prediction")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.show()
