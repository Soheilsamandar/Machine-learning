<h1 align="center">🛒 Store Sales Prediction</h1>

<h3 align="center">
Machine Learning Regression Project for Predicting Store Sales
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
Store Sales Prediction is a Machine Learning regression project that predicts
future sales of a store based on historical sales data and different business
factors.
</p>

<p>
The main goal of this project is to analyze previous sales patterns and build
a model that can estimate future revenue.
</p>

<p>
This type of prediction helps businesses make better decisions about inventory,
marketing strategies, and resource management.
</p>

<hr>

<h2>🎯 What We Are Going To Do</h2>

<ul>

<li>Analyze historical store sales data</li>

<li>Understand sales patterns and trends</li>

<li>Clean and preprocess the dataset</li>

<li>Select important business features</li>

<li>Train a Machine Learning regression model</li>

<li>Evaluate prediction accuracy</li>

<li>Predict future sales</li>

</ul>

<hr>

<h2>📊 Dataset</h2>

<p>
The dataset contains historical information about store transactions and sales.
Each row represents a sales record.
</p>


<table border="1">

<tr>
<th>Feature</th>
<th>Description</th>
</tr>

<tr>
<td>Date</td>
<td>Sales transaction date</td>
</tr>

<tr>
<td>Store ID</td>
<td>Store identification number</td>
</tr>

<tr>
<td>Product Category</td>
<td>Type of product sold</td>
</tr>

<tr>
<td>Number of Customers</td>
<td>Daily customer count</td>
</tr>

<tr>
<td>Advertising</td>
<td>Marketing investment</td>
</tr>

<tr>
<td>Previous Sales</td>
<td>Historical sales amount</td>
</tr>

<tr>
<td>Total Sales</td>
<td>Target value to predict</td>
</tr>

</table>


<h3 align="left">
Dataset Preview
</h3>


<p align="left">

<img src="./img/dataset5.webp" width="700">

</p>

<hr>

<h2>🧠 Machine Learning Model</h2>

<h3>Random Forest Regression</h3>


<p>
Random Forest Regression is used for this project because store sales depend
on many different factors and the relationship between features and sales is
usually not completely linear.
</p>


<p>
Random Forest combines multiple decision trees and creates a stronger model
with better prediction ability.
</p>


<pre>

Input:

Previous Sales = 5000
Customers = 300
Advertising = High


Output:

Predicted Sales = 6500

</pre>


<hr>

<h2>❓ Why This Model?</h2>

<ul>

<li>Sales patterns are complex and nonlinear.</li>

<li>Multiple factors affect business revenue.</li>

<li>Random Forest handles many features effectively.</li>

<li>It reduces overfitting compared to a single decision tree.</li>

<li>It can measure feature importance.</li>

</ul>


<hr>

<h2>🧮 Mathematical Explanation</h2>


<p>
Random Forest is based on Decision Trees.
Each tree makes a prediction and the final output is the average of all trees.
</p>


<p align="center">

<b>
Prediction = (Tree₁ + Tree₂ + Tree₃ + ... + Treeₙ) / n
</b>

</p>


<h3>Decision Tree Splitting</h3>


<p>
The tree chooses the best feature split using variance reduction.
</p>


<p align="center">

<b>
Variance = (1/n) Σ(x - x̄)²
</b>

</p>


<p>
The algorithm selects splits that reduce prediction error.
</p>


<h3>Mean Squared Error</h3>


<p align="center">

<b>
MSE = (1/n) Σ(y - ŷ)²
</b>

</p>


<p>
Each tree tries to minimize this error during training.
</p>


<hr>

<h2>⚙ Model Learning Process</h2>


<ul>

<li>Create multiple decision trees from random samples of data</li>

<li>Train each tree independently</li>

<li>Each tree learns different patterns</li>

<li>Combine all predictions</li>

<li>Generate final sales prediction</li>

</ul>


<p>
The randomness of trees helps the model become more accurate and prevents
overfitting.
</p>


<hr>

<h2>📈 Model Evaluation</h2>


<h3>MAE (Mean Absolute Error)</h3>

<p>
Measures average prediction difference.
</p>


<p align="center">

<b>
MAE = (1/n) Σ|y - ŷ|
</b>

</p>


<h3>RMSE (Root Mean Squared Error)</h3>

<p>
Penalizes larger sales prediction errors.
</p>


<p align="center">

<b>
RMSE = √((1/n)Σ(y - ŷ)²)
</b>

</p>


<h3>R² Score</h3>

<p>
Shows how well the model explains sales variations.
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

Store-Sales-Prediction
│
├── dataset_generator.py
│
├── img
│   └── dataset.webp
│
├── models.pkl
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

<li>Use XGBoost and Gradient Boosting</li>

<li>Add time-series forecasting models</li>

<li>Predict seasonal sales trends</li>

<li>Create business analytics dashboard</li>

<li>Deploy real-time sales prediction system</li>

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