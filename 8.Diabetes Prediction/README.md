<h1 align="center">🩺 Diabetes Prediction</h1>

<h3 align="center">
Machine Learning Classification Project for Predicting Diabetes Risk
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
Diabetes Prediction is a Machine Learning classification project that predicts
whether a person has a risk of diabetes based on medical and health-related
features.
</p>

<p>
The purpose of this project is to analyze health data and build an AI model
that can assist in early diabetes risk detection.
</p>

<p>
Machine Learning can help healthcare systems identify high-risk patients and
provide earlier medical attention.
</p>


<hr>


<h2>🎯 What We Are Going To Do</h2>

<ul>

<li>Analyze diabetes dataset</li>

<li>Understand relationships between health features</li>

<li>Clean and preprocess medical data</li>

<li>Select important features</li>

<li>Train a classification model</li>

<li>Evaluate prediction performance</li>

<li>Predict diabetes risk for new patients</li>

</ul>


<hr>


<h2>📊 Dataset</h2>

<p>
The dataset contains medical information about individuals and their diabetes
status.
</p>


<table border="1">

<tr>
<th>Feature</th>
<th>Description</th>
</tr>


<tr>
<td>Pregnancies</td>
<td>Number of pregnancies</td>
</tr>


<tr>
<td>Glucose</td>
<td>Blood glucose level</td>
</tr>


<tr>
<td>Blood Pressure</td>
<td>Blood pressure measurement</td>
</tr>


<tr>
<td>BMI</td>
<td>Body Mass Index</td>
</tr>


<tr>
<td>Age</td>
<td>Person age</td>
</tr>


<tr>
<td>Insulin</td>
<td>Insulin level</td>
</tr>


<tr>
<td>Diabetes</td>
<td>Target class (Yes / No)</td>
</tr>


</table>


<h3 align="left">
Dataset Preview
</h3>


<p align="left">

<img src="./img/dataset8.webp" width="700">

</p>


<hr>


<h2>🧠 Machine Learning Model</h2>


<h3>Logistic Regression</h3>


<p>
Logistic Regression is used to classify patients into two groups:
</p>


<pre>

0 → No Diabetes

1 → Diabetes

</pre>


<p>
The model calculates the probability of diabetes based on medical features.
</p>


<hr>


<h2>❓ Why This Model?</h2>


<ul>

<li>The problem is a binary classification problem.</li>

<li>The output has only two classes.</li>

<li>The model provides probability estimation.</li>

<li>The mathematical process is easy to interpret.</li>

<li>It is widely used for medical classification tasks.</li>

</ul>


<hr>


<h2>🧮 Mathematical Explanation</h2>


<p>
Logistic Regression first calculates a linear combination of input features.
</p>


<p align="center">

<b>
z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
</b>

</p>


<p>
Then it converts this value into probability using the Sigmoid Function.
</p>


<p align="center">

<b>
σ(z) = 1 / (1 + e⁻ᶻ)
</b>

</p>


<table border="1">

<tr>
<th>Symbol</th>
<th>Meaning</th>
</tr>


<tr>
<td>x</td>
<td>Medical features</td>
</tr>


<tr>
<td>w</td>
<td>Feature weights</td>
</tr>


<tr>
<td>b</td>
<td>Bias</td>
</tr>


<tr>
<td>σ(z)</td>
<td>Diabetes probability</td>
</tr>


</table>


<p>
If the probability is higher than 0.5, the model predicts diabetes risk.
</p>


<hr>


<h2>⚙ Model Learning Process</h2>


<p>
During training, the model adjusts weights to create the best separation between
diabetes and non-diabetes cases.
</p>


<h3>Binary Cross Entropy Loss</h3>


<p align="center">

<b>
Loss = -[y log(p) + (1-y) log(1-p)]
</b>

</p>


<table border="1">

<tr>
<th>Symbol</th>
<th>Meaning</th>
</tr>


<tr>
<td>y</td>
<td>Actual class</td>
</tr>


<tr>
<td>p</td>
<td>Predicted probability</td>
</tr>


</table>


<p>
The training goal is minimizing classification error.
</p>


<hr>


<h2>📈 Model Evaluation</h2>


<h3>Accuracy</h3>

<p>
Shows the percentage of correct predictions.
</p>


<p align="center">

<b>
Accuracy = Correct Predictions / Total Predictions
</b>

</p>


<h3>Precision</h3>

<p>
Measures how many predicted diabetes cases were actually correct.
</p>


<h3>Recall</h3>

<p>
Measures how many real diabetes cases were detected.
</p>


<h3>F1 Score</h3>

<p>
Balances precision and recall.
</p>


<h3>Confusion Matrix</h3>

<p>
Shows the number of correct and incorrect classifications.
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

Diabetes-Prediction
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

<li>Use Random Forest and XGBoost models</li>

<li>Add medical feature analysis</li>

<li>Create health risk prediction dashboard</li>

<li>Use Deep Learning approaches</li>

<li>Deploy as a healthcare AI assistant</li>

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