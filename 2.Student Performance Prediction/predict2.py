import joblib
import pandas as pd

model = joblib.load("2.Student Performance Prediction/student_model.pkl")


print("Student Performance Prediction")
print("------------------------------")


study = int(input("Study hours: "))


attendance = int(input("Attendance percentage: "))


midterm = int(input("Midterm score: "))


homework = int(input("Homework score: "))


sleep = int(input("Sleep hours: "))


student = pd.DataFrame(
    {
        "Study_hours": [study],
        "Attedance": [attendance],
        "Midterm_score": [midterm],
        "Homework": [homework],
        "Sleep_Hours": [sleep]
    }
)


result = model.predict(student)

if result[0] == 1:

    print("\nStudent will PASS")
else:
    print("\nStudent will FAIL")
