import pandas as pd
import joblib

model = joblib.load("9.Iris Flower Classification\iris_model.pkl")


print("Iris Flower Classification")

print("--------------------------")


sepal_length = float(input("Sepal Length: "))


sepal_width = float(input("Sepal Width: "))


petal_length = float(input("Petal Length: "))


petal_width = float(input("Petal Width: "))


flower = pd.DataFrame(
    {
        "SepalLength": [sepal_length],
        "SepalWidth": [sepal_width],
        "PetalLength": [petal_length],
        "PetalWidth": [petal_width],
    }
)


prediction = model.predict(flower)


classes = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}


print("Predicted Flower:", classes[prediction[0]])
