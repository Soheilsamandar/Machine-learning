<h1 align="center">🏠 House Price Prediction</h1>

<h3 align="center">
Machine Learning Regression Project for Predicting House Prices
</h3>

<p align="center">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white">
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white">
<img src="https://img.shields.io/badge/Machine%20Learning-0A66C2?style=for-the-badge">
</p>

<hr>

<h2>📖 Project Overview</h2>

<p>
House Price Prediction is a Machine Learning regression project that predicts
the price of residential properties based on different housing features.
</p>

<p>
The main goal of this project is to build a model that learns the relationship
between house characteristics and their market value, then predicts the price
of new houses.
</p>

<p>
This project demonstrates the complete Machine Learning workflow:
</p>

<ul>
<li>Data Analysis</li>
<li>Data Preprocessing</li>
<li>Feature Selection</li>
<li>Model Training</li>
<li>Model Evaluation</li>
<li>Price Prediction</li>
</ul>

<hr>

<h2>🎯 What We Are Going To Do</h2>

<ul>
<li>Load and analyze the housing dataset</li>
<li>Understand relationships between features</li>
<li>Clean and prepare the data</li>
<li>Select important features</li>
<li>Train a Machine Learning model</li>
<li>Evaluate model performance</li>
<li>Predict prices for new houses</li>
</ul>

<hr>

<h2>📊 Dataset</h2>

<p>
The dataset contains information about houses and their prices.
Each row represents one house and each column represents a feature.
</p>

<table border="1">

<tr>
<th>Feature</th>
<th>Description</th>
</tr>

<tr>
<td>Area</td>
<td>Total size of the house</td>
</tr>

<tr>
<td>Bedrooms</td>
<td>Number of bedrooms</td>
</tr>

<tr>
<td>Bathrooms</td>
<td>Number of bathrooms</td>
</tr>

<tr>
<td>Location</td>
<td>Geographical location of the house</td>
</tr>

<tr>
<td>Age</td>
<td>Age of the building</td>
</tr>

<tr>
<td>Price</td>
<td>Target value to predict</td>
</tr>

</table>


<h3 align="left">Dataset Preview</h3>

<p align="left">
<img src="./img/dataset1.webp" width="700">
</p>

<hr>

<h2>🧠 Machine Learning Model</h2>

<h3>Linear Regression</h3>

<p>
Linear Regression is used as the main prediction model.
The purpose of this model is to find a mathematical relationship between
house features and house prices.
</p>


<hr>

<h2>❓ Why Linear Regression?</h2>

<p>
House price prediction is a Regression Problem because the output is a continuous
numerical value.
</p>

<ul>
<li>The target value is a price.</li>
<li>The relationship between features and price can be modeled mathematically.</li>
<li>The model is simple and easy to interpret.</li>
<li>The effect of each feature can be analyzed using weights.</li>
</ul>


<hr>

<h2>🧮 Mathematical Explanation</h2>

<p>
Linear Regression tries to find the best equation that represents the relationship
between input features and output price.
</p>


<p align="center">

<b>
y = w₁x₁ + w₂x₂ + w₃x₃ + ... + wₙxₙ + b
</b>

</p>


<table border="1">

<tr>
<th>Symbol</th>
<th>Meaning</th>
</tr>

<tr>
<td>y</td>
<td>Predicted house price</td>
</tr>

<tr>
<td>x</td>
<td>Input features</td>
</tr>

<tr>
<td>w</td>
<td>Weight of each feature</td>
</tr>

<tr>
<td>b</td>
<td>Bias value</td>
</tr>

</table>


<p>
Example:
</p>

<p align="center">

<b>
Price = w₁(Area) + w₂(Rooms) + w₃(Location) + b
</b>

</p>


<p>
The model learns the values of weights to understand how each feature affects
the final house price.
</p>


<hr>

<h2>⚙ Model Learning Process</h2>

<p>
At the beginning, the model does not know the correct weights.
It starts with random values and improves them through training.
</p>

<p>
The model predicts prices and calculates the difference between predicted values
and real values.
</p>


<h3>Mean Squared Error (MSE)</h3>

<p align="center">

<b>
MSE = (1/n) Σ(y - ŷ)²
</b>

</p>


<table border="1">

<tr>
<th>Symbol</th>
<th>Meaning</th>
</tr>

<tr>
<td>y</td>
<td>Actual house price</td>
</tr>

<tr>
<td>ŷ</td>
<td>Predicted house price</td>
</tr>

<tr>
<td>n</td>
<td>Number of samples</td>
</tr>

</table>


<p>
The goal of training is minimizing the error:
</p>

<p align="center">

<b>
Minimize(MSE)
</b>

</p>


<h3>Gradient Descent</h3>

<p>
Weights are updated using Gradient Descent:
</p>


<p align="center">

<b>
w = w - α ∂J(w)/∂w
</b>

</p>


<ul>
<li>α = Learning Rate</li>
<li>J(w) = Cost Function</li>
</ul>


<hr>

<h2>📈 Model Evaluation</h2>

<h3>MAE (Mean Absolute Error)</h3>

<p>
Measures the average difference between predicted and real prices.
</p>


<p align="center">

<b>
MAE = (1/n) Σ |y - ŷ|
</b>

</p>


<h3>RMSE (Root Mean Squared Error)</h3>

<p>
Shows larger prediction errors more clearly.
</p>


<p align="center">

<b>
RMSE = √((1/n) Σ(y - ŷ)²)
</b>

</p>


<h3>R² Score</h3>

<p>
Shows how well the model explains the changes in house prices.
</p>


<hr>

<h2>🛠 Technologies Used</h2>

<ul>
<li>Python</li>
<li>Pandas</li>
<li>NumPy</li>
<li>Scikit-Learn</li>
<li>Matplotlib</li>
</ul>


<hr>

<h2>📂 Project Structure</h2>

<pre>

House-Price-Prediction

│
├── dataset_generator.py
│
├── models.pkl
│
├── dataset.csv
│
├── train.py
│
├── predict.py
│
└── README.md

</pre>


<hr>

<h2>🚀 Future Improvements</h2>

<ul>
<li>Use advanced regression algorithms</li>
<li>Apply feature engineering techniques</li>
<li>Improve accuracy using hyperparameter tuning</li>
<li>Deploy the model as a web application</li>
<li>Add more real-world housing features</li>
</ul>


<hr>

<h2>👨‍💻 Author</h2>

<p align="center">

<a href="https://github.com/Soheilsamandar">
<img src="https://img.shields.io/badge/Soheil_Samandar-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

<a href="https://github.com/AlphaRoboticsTeam">
<img src="https://img.shields.io/badge/Alpha_Robotics_Team-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

</p>


<p align="center">
⭐ Learning Machine Learning by Building Real Projects 🚀
</p>
