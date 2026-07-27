import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


df = pd.read_csv(r"1.House Price Prediction/house_price.csv")
print("First 5 Rows")
print(df.head())

print("\n Dataset information ")
print(df.info())

# Feature
X = df.drop("Price", axis=1)


# Lables
y = df["Price"]

x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = LinearRegression()
model.fit(x_train,y_train)
predictions = model.predict(x_test)

mae = mean_absolute_error(y_test,predictions)
mse = mean_squared_error(y_test,predictions)
r2 = r2_score(y_test,predictions)


print("\n Model Evaluation")
print("--------------------")
print("MAE :",mae)
print("MSE :", mse)
print("R2 :", r2)

print("\nFeature Importance")

for feature , coef in zip(X.columns,model.coef_):
    print(feature , ":" , round(coef,2))


print("\nIntercept : ",model.intercept_)


joblib.dump(model,"1.House Price Prediction/house_model.pkl")
print("\nModel saved successfully")
