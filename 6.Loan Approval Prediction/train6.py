import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

df = pd.read_csv("6.Loan Approval Prediction\loan_dataset.csv")

X = df.drop("LoanStatus", axis=1)

y = df["LoanStatus"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
}


best_model = None
best_score = 0


for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(y_test, prediction)

    print(name)
    print("Accuracy:", accuracy)
    print("--------------------")

    if accuracy > best_score:

        best_score = accuracy

        best_model = model


joblib.dump(best_model, "6.Loan Approval Prediction\loan_model.pkl")

print("Best Model Saved")
