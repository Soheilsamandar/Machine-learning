import pandas as pd
import random

data = []

for i in range(1000):

    study_hours = random.randint(0, 10)

    attendance = random.randint(50, 100)

    midterm_score = random.randint(0, 20)

    homework = random.randint(0, 10)

    sleep_hours = random.randint(4, 10)

    score = (
        study_hours * 2
        + attendance * 0.05
        + midterm_score * 2
        + homework * 1.5
        + sleep_hours * 0.5
    )

    if score >= 45:
        result = 1  # Pass
    else:
        result = 0  # Fail

    data.append([study_hours, attendance, midterm_score, homework, sleep_hours, score, result])
columns = [
    "Study_Hours",
    "Attendance",
    "Midterm_Score",
    "Homework",
    "Sleep_Hours",
    "Score",
    "Result",
]
df = pd.DataFrame(data, columns=columns)
df.to_csv("2.Student Performance Prediction\student_performance.csv", index=False)
print(df.head())
print("\nDataset Created Successfully!")
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Score"], color="blue", alpha=0.7)
plt.title("Student Performance Dataset")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.grid(True)
plt.show()
