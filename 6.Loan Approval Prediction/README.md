<h1 align="center">🏦 Loan Approval Prediction</h1>

<h3 align="center">
Machine Learning Classification Project for Predicting Loan Approval Decisions
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
Loan Approval Prediction is a Machine Learning classification project that
predicts whether a customer's loan application will be approved or rejected.
</p>

<p>
The model analyzes financial and personal information of applicants and learns
patterns from previous loan decisions.
</p>

<p>
This type of system can help banks and financial institutions make faster and
more accurate decisions while reducing human errors.
</p>


<hr>


<h2>🎯 What We Are Going To Do</h2>

<ul>

<li>Analyze customer loan dataset</li>

<li>Understand important factors affecting loan approval</li>

<li>Clean and preprocess data</li>

<li>Convert categorical data into numerical values</li>

<li>Train a classification model</li>

<li>Evaluate model performance</li>

<li>Predict loan approval for new customers</li>

</ul>


<hr>


<h2>📊 Dataset</h2>

<p>
The dataset contains information about customers and their loan applications.
Each row represents one applicant.
</p>


<table border="1">

<tr>
<th>Feature</th>
<th>Description</th>
</tr>


<tr>
<td>Gender</td>
<td>Applicant gender</td>
</tr>


<tr>
<td>Age</td>
<td>Customer age</td>
</tr>


<tr>
<td>Income</td>
<td>Monthly income</td>
</tr>


<tr>
<td>Loan Amount</td>
<td>Requested loan value</td>
</tr>


<tr>
<td>Credit Score</td>
<td>Customer credit history score</td>
</tr>


<tr>
<td>Employment Status</td>
<td>Job and employment information</td>
</tr>


<tr>
<td>Loan Status</td>
<td>Approved or Rejected</td>
</tr>


</table>


<h3 align="left">
Dataset Preview
</h3>


<p align="left">

<img src="./img/dataset6.webp" width="700">

</p>


<hr>


<h2>🧠 Machine Learning Model</h2>


<h3>Logistic Regression</h3>


<p>
Logistic Regression is used for this classification problem.
The model predicts the probability of loan approval based on applicant features.
</p>


<p>
Output:
</p>


<pre>

0 → Loan Rejected

1 → Loan Approved

</pre>


<hr>


<h2>❓ Why This Model?</h2>


<p>
Loan approval prediction is a Binary Classification problem because the output
has only two possible classes.
</p>


<ul>

<li>The output is categorical.</li>

<li>The model provides probability estimation.</li>

<li>It is fast and efficient.</li>

<li>The mathematical decision boundary can be interpreted.</li>

<li>It works well for financial classification problems.</li>

</ul>


<hr>


<h2>🧮 Mathematical Explanation</h2>


<p>
Logistic Regression uses the Sigmoid Function to convert predictions into
probabilities.
</p>


<p align="center">

<b>
σ(z) = 1 / (1 + e⁻ᶻ)
</b>

</p>


<p>
Where:
</p>


<table border="1">

<tr>
<th>Symbol</th>
<th>Meaning</th>
</tr>


<tr>
<td>z</td>
<td>Linear combination of features</td>
</tr>


<tr>
<td>e</td>
<td>Euler's number</td>
</tr>


<tr>
<td>σ(z)</td>
<td>Probability of approval</td>
</tr>


</table>


<p>
The linear equation:
</p>


<p align="center">

<b>
z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b
</b>

</p>


<p>
If the probability is higher than 0.5, the model predicts approval.
</p>


<hr>


<h2>⚙ Model Learning Process</h2>


<p>
During training, the model adjusts weights to separate approved and rejected
applications.
</p>


<p>
The model uses Cross Entropy Loss:
</p>


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
The goal is minimizing classification error.
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
Measures how many approved predictions were actually correct.
</p>


<h3>Recall</h3>

<p>
Measures how many real approved loans were detected.
</p>


<h3>F1 Score</h3>

<p>
Balances precision and recall.
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

Loan-Approval-Prediction
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

<li>Use Random Forest Classifier</li>

<li>Use XGBoost for better accuracy</li>

<li>Add explainable AI techniques</li>

<li>Create banking decision dashboard</li>

<li>Deploy as a loan evaluation API</li>

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