import pandas as pd
import random

data = []


for i in range(1000):

    customers = random.randint(20, 500)

    price = random.randint(10, 200)

    advertising = random.randint(0, 100)

    discount = random.randint(0, 50)

    stock = random.randint(10, 1000)

    day = random.randint(1, 7)

    sales = (
        customers * 5
        - price * 2
        + advertising * 10
        + discount * 3
        + stock * 0.5
        + random.randint(-500, 500)
    )

    data.append([customers, price, advertising, discount, stock, day, sales])


columns = ["Customers", "Price", "Advertising", "Discount", "Stock", "Day", "Sales"]


df = pd.DataFrame(data, columns=columns)


df.to_csv(r"5.Store Sales Prediction\store_sales.csv", index=False)


print(df.head())

print("\nDataset Created Successfully!")

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.scatter(df["Customers"], df["Sales"], alpha=0.6, color="purple")
plt.title("Store Sales Prediction")
plt.xlabel("Customers")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
