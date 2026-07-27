<h1 align="center">🎓 Student Performance Prediction</h1>

<h3 align="center">
Machine Learning Project for Predicting Student Academic Performance
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
Student Performance Prediction is a Machine Learning project that predicts
students' academic performance based on different educational, personal,
and behavioural factors.
</p>

<p>
The goal of this project is to understand how different factors such as
study time, attendance, previous scores, and learning conditions affect
student results.
</p>

<p>
Using Machine Learning, we create a predictive model that can estimate
a student's final performance and help identify students who may need
additional educational support.
</p>


<hr>

<h2>🎯 What We Are Going To Do</h2>

<ul>

<li>Analyze student dataset</li>

<li>Understand relationships between features</li>

<li>Clean and preprocess the data</li>

<li>Select important features</li>

<li>Train a Machine Learning model</li>

<li>Evaluate prediction accuracy</li>

<li>Predict student final performance</li>

</ul>


<hr>

<h2>📊 Dataset</h2>

<p>
The dataset contains information about students and their academic results.
Each sample represents one student with different educational features.
</p>


<table border="1">

<tr>
<th>Feature</th>
<th>Description</th>
</tr>


<tr>
<td>Study Time</td>
<td>Number of hours spent studying</td>
</tr>


<tr>
<td>Attendance</td>
<td>Percentage of class attendance</td>
</tr>


<tr>
<td>Previous Scores</td>
<td>Previous academic results</td>
</tr>


<tr>
<td>Sleep Hours</td>
<td>Average sleeping duration</td>
</tr>


<tr>
<td>Internet Access</td>
<td>Availability of online learning resources</td>
</tr>


<tr>
<td>Parental Education</td>
<td>Education level of parents</td>
</tr>


<tr>
<td>Final Score</td>
<td>Target value to predict</td>
</tr>


</table>


<h3 align="left">
Dataset Preview
</h3>


<p align="left">

<img src="./img/dataset2.webp" width="700">

</p>


<hr>


<h2>🧠 Machine Learning Model</h2>


<h3>Linear Regression</h3>


<p>
Linear Regression is used to predict the final score of students.
The model learns the relationship between educational factors and student results.
</p>


<p>
Example:
</p>


<pre>

Input:

Study Time = 15 hours/week
Attendance = 90%
Previous Score = 85


Output:

Predicted Final Score = 88

</pre>


<hr>


<h2>❓ Why Linear Regression?</h2>


<p>
This problem is a Regression Problem because the output is a continuous
numerical value (student score).
</p>


<ul>

<li>The final score is a numerical value.</li>

<li>The model can measure the effect of each feature.</li>

<li>The relationship between learning factors and performance can be modeled mathematically.</li>

<li>The algorithm is simple and interpretable.</li>

</ul>


<hr>


<h2>🧮 Mathematical Explanation</h2>


<p>
Linear Regression finds a mathematical function that maps student features
to the final score.
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

<td>Predicted student score</td>

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
Score = w₁(StudyTime) + w₂(Attendance) + w₃(PreviousScore) + b
</b>

</p>


<p>
The model learns the weights to understand which factors have more impact
on student performance.
</p>


<hr>


<h2>⚙ Model Learning Process</h2>


<p>
During training, the model starts with unknown parameters.
It makes predictions and compares them with actual student scores.
</p>


<p>
The difference between prediction and reality is calculated using a loss function.
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

<td>Actual student score</td>

</tr>


<tr>

<td>ŷ</td>

<td>Predicted score</td>

</tr>


<tr>

<td>n</td>

<td>Number of students</td>

</tr>


</table>


<p>
The goal of training is:
</p>


<p align="center">

<b>
Minimize(MSE)
</b>

</p>



<h3>Gradient Descent</h3>


<p>
The model updates weights using Gradient Descent:
</p>


<p align="center">

<b>
w = w - α ∂J(w)/∂w
</b>

</p>


<ul>

<li>α : Learning Rate</li>

<li>J(w) : Cost Function</li>

</ul>


<hr>


<h2>📈 Model Evaluation</h2>


<h3>MAE (Mean Absolute Error)</h3>


<p>
Measures the average difference between predicted and actual scores.
</p>


<p align="center">

<b>
MAE = (1/n) Σ|y - ŷ|
</b>

</p>



<h3>RMSE (Root Mean Squared Error)</h3>


<p>
Shows larger prediction errors more clearly.
</p>


<p align="center">

<b>
RMSE = √((1/n)Σ(y - ŷ)²)
</b>

</p>



<h3>R² Score</h3>


<p>
Measures how well the model explains changes in student performance.
</p>


<hr>


<h2>🛠 Technologies Used</h2>


<ul>

<li>Python</li>

<li>Pandas</li>

<li>NumPy</li>

<li>Scikit-Learn</li>

<li>Matplotlib</li>

<li>Jupyter Notebook</li>

</ul>


<hr>


<h2>📂 Project Structure</h2>


<pre>

Student-Performance-Prediction

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

<li>Use advanced models like Random Forest and XGBoost</li>

<li>Add more educational features</li>

<li>Create student risk prediction system</li>

<li>Build an interactive dashboard</li>

<li>Deploy the model as an AI educational assistant</li>

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