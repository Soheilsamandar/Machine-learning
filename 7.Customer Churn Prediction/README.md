<h1 align="center">👥 Customer Churn Prediction</h1>

<h3 align="center">
Machine Learning Classification Project for Predicting Customer Retention
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
Customer Churn Prediction is a Machine Learning classification project that
predicts whether a customer will leave a service or continue using it.
</p>

<p>
Customer churn is an important problem for companies because losing customers
can reduce revenue and increase business costs.
</p>

<p>
The goal of this project is to analyze customer behavior and build a model
that identifies customers who have a high probability of leaving.
</p>


<hr>


<h2>🎯 What We Are Going To Do</h2>

<ul>

<li>Analyze customer behavior dataset</li>

<li>Find important factors affecting customer churn</li>

<li>Clean and preprocess data</li>

<li>Convert categorical features into numerical values</li>

<li>Train a Machine Learning classification model</li>

<li>Evaluate model performance</li>

<li>Predict future customer churn</li>

</ul>


<hr>


<h2>📊 Dataset</h2>

<p>
The dataset contains information about customers and their interaction with
a company service.
</p>


<table border="1">

<tr>
<th>Feature</th>
<th>Description</th>
</tr>


<tr>
<td>Age</td>
<td>Customer age</td>
</tr>


<tr>
<td>Gender</td>
<td>Customer gender</td>
</tr>


<tr>
<td>Monthly Charges</td>
<td>Amount paid monthly</td>
</tr>


<tr>
<td>Contract Type</td>
<td>Customer subscription type</td>
</tr>


<tr>
<td>Usage Time</td>
<td>Service usage duration</td>
</tr>


<tr>
<td>Support Calls</td>
<td>Number of customer support requests</td>
</tr>


<tr>
<td>Churn</td>
<td>Customer leaving status</td>
</tr>


</table>


<h3 align="left">
Dataset Preview
</h3>

<p align="left">
<img src="./img/dataset7.webp" width="700">
</p>


<hr>


<h2>🧠 Machine Learning Model</h2>


<h3>Random Forest Classifier</h3>


<p>
Random Forest Classifier is used to predict whether a customer will leave or
stay.
</p>

<p>
The algorithm creates multiple decision trees and combines their results to
produce a more accurate prediction.
</p>


<pre>

Input:

Contract = Monthly
Support Calls = High
Usage Time = Low


Output:

Churn = Yes

</pre>


<hr>


<h2>❓ Why This Model?</h2>


<ul>

<li>Customer behavior is usually complex and nonlinear.</li>

<li>Random Forest can handle many different features.</li>

<li>It reduces overfitting compared to a single decision tree.</li>

<li>It provides feature importance information.</li>

<li>It works well with classification problems.</li>

</ul>


<hr>


<h2>🧮 Mathematical Explanation</h2>


<p>
Random Forest is based on multiple Decision Trees.
Each tree gives a prediction and the final result is selected by voting.
</p>


<p align="center">

<b>
Final Prediction = Majority Vote(Tree Predictions)
</b>

</p>


<h3>Gini Impurity</h3>


<p>
Decision trees select the best split using Gini impurity.
</p>


<p align="center">

<b>
Gini = 1 - Σp²
</b>

</p>


<table border="1">

<tr>
<th>Symbol</th>
<th>Meaning</th>
</tr>


<tr>
<td>p</td>
<td>Probability of each class</td>
</tr>

</table>


<p>
The algorithm chooses splits that reduce impurity and create better separated
classes.
</p>


<hr>


<h2>⚙ Model Learning Process</h2>


<ul>

<li>Create multiple decision trees</li>

<li>Use random samples from the dataset</li>

<li>Train each tree independently</li>

<li>Combine predictions from all trees</li>

<li>Generate final churn prediction</li>

</ul>


<p>
The combination of many models improves accuracy and stability.
</p>


<hr>


<h2>📈 Model Evaluation</h2>


<h3>Accuracy</h3>

<p>
Measures the percentage of correct predictions.
</p>


<p align="center">

<b>
Accuracy = Correct Predictions / Total Predictions
</b>

</p>


<h3>Precision</h3>

<p>
Measures how many predicted churn customers were actually churn customers.
</p>


<h3>Recall</h3>

<p>
Measures how many real churn customers were successfully detected.
</p>


<h3>F1 Score</h3>

<p>
Combines precision and recall into one metric.
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

Customer-Churn-Prediction
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

<li>Add customer behavior analysis</li>

<li>Create customer retention recommendation system</li>

<li>Build real-time churn prediction dashboard</li>

<li>Deploy as a business AI solution</li>

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