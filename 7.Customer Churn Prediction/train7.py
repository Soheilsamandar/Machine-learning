import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("7.Customer Churn Prediction\customer_churn.csv")

X = df.drop("Churn", axis=1)

y = df["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Accuracy")

print(accuracy_score(y_test, prediction))

joblib.dump(model, "7.Customer Churn Prediction\customer_model.pkl")
