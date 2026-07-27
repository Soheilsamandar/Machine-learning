import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

df = pd.read_csv("8.Diabetes Prediction\diabetes_dataset.csv")

X = df.drop("Diabetes", axis=1)

y = df["Diabetes"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=150, random_state=42)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Accuracy:")

print(accuracy_score(y_test, prediction))

joblib.dump(model, "8.Diabetes Prediction\diabetes_model.pkl")

print("Model Saved")
