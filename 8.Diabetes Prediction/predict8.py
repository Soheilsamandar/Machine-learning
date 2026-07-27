import pandas as pd
import joblib

model = joblib.load("8.Diabetes Prediction\diabetes_model.pkl")

pregnancies = int(input("Pregnancies: "))

glucose = int(input("Glucose: "))

bp = int(input("Blood Pressure: "))

skin = int(input("Skin Thickness: "))

insulin = int(input("Insulin: "))

bmi = float(input("BMI: "))

age = int(input("Age: "))

person = pd.DataFrame(
    {
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [bp],
        "SkinThickness": [skin],
        "Insulin": [insulin],
        "BMI": [bmi],
        "Age": [age],
    }
)

prediction = model.predict(person)

if prediction[0] == 1:

    print("High Risk Of Diabetes")

else:

    print("Low Risk Of Diabetes")
