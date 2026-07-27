import pandas as pd
import joblib


from sklearn.model_selection import train_test_split


from sklearn.preprocessing import StandardScaler


from sklearn.pipeline import Pipeline


from sklearn.neighbors import KNeighborsClassifier


from sklearn.metrics import accuracy_score

df = pd.read_csv("9.Iris Flower Classification\iris_dataset.csv")


X = df.drop("Species", axis=1)


y = df["Species"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = Pipeline(
    [("scaler", StandardScaler()), ("knn", KNeighborsClassifier(n_neighbors=5))]
)


model.fit(X_train, y_train)


prediction = model.predict(X_test)


accuracy = accuracy_score(y_test, prediction)


print("Accuracy:", accuracy)


joblib.dump(model, "9.Iris Flower Classification\iris_model.pkl")


print("Model Saved")
