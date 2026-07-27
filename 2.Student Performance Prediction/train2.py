import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("2.Student Performance Prediction\student_performance.csv")
print(df.head())


# Features
X = df.drop("Result", axis=1)


# Label
y = df["Result"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Create model
model = LogisticRegression()


# Train
model.fit(X_train, y_train)


# Prediction
y_pred = model.predict(X_test)


# Evaluation
print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# Save model
joblib.dump(model, "2.Student Performance Prediction\student_model.pkl")
print("\nModel Saved!")
