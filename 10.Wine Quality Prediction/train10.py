import pandas as pd
import joblib


from sklearn.model_selection import train_test_split


from sklearn.ensemble import RandomForestRegressor


from sklearn.tree import DecisionTreeRegressor


from sklearn.linear_model import LinearRegression


from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("10.Wine Quality Prediction\wine_quality.csv")


X = df.drop("Quality", axis=1)


y = df["Quality"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
}


best_model = None

best_score = -999


for name, model in models.items():

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    mae = mean_absolute_error(y_test, prediction)

    score = r2_score(y_test, prediction)

    print("\nModel:", name)

    print("MAE:", mae)

    print("R2 Score:", score)

    if score > best_score:

        best_score = score

        best_model = model


joblib.dump(best_model, "10.Wine Quality Prediction\wine_model.pkl")


print("\nBest Model Saved")

print("Score:", best_score)
