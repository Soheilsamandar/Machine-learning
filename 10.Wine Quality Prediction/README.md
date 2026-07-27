<h1 align="center">🍷 Wine Quality Prediction</h1>

<h3 align="center">
Machine Learning Classification & Regression Project for Predicting Wine Quality
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
Wine Quality Prediction is a Machine Learning project that predicts the quality
of wine based on its chemical properties.
</p>

<p>
The goal of this project is to analyze the relationship between wine
characteristics and quality scores, then build a model that can estimate the
quality of unknown wine samples.
</p>

<p>
This project demonstrates how Machine Learning can be used in the food and
beverage industry for quality control and automated evaluation.
</p>


<hr>


<h2>🎯 What We Are Going To Do</h2>

<ul>

<li>Analyze wine quality dataset</li>

<li>Understand the relationship between chemical properties and quality</li>

<li>Clean and preprocess data</li>

<li>Select important features</li>

<li>Train Machine Learning models</li>

<li>Evaluate model performance</li>

<li>Predict quality of new wine samples</li>

</ul>


<hr>


<h2>📊 Dataset</h2>

<p>
The dataset contains chemical measurements of different wine samples and their
quality scores.
</p>


<table border="1">

<tr>
<th>Feature</th>
<th>Description</th>
</tr>


<tr>
<td>Fixed Acidity</td>
<td>Amount of fixed acids in wine</td>
</tr>


<tr>
<td>Volatile Acidity</td>
<td>Amount of volatile acids</td>
</tr>


<tr>
<td>Citric Acid</td>
<td>Citric acid concentration</td>
</tr>


<tr>
<td>Sugar</td>
<td>Residual sugar amount</td>
</tr>


<tr>
<td>Alcohol</td>
<td>Alcohol percentage</td>
</tr>


<tr>
<td>pH</td>
<td>Acidity level</td>
</tr>


<tr>
<td>Quality</td>
<td>Wine quality score</td>
</tr>


</table>


<h3 align="left">
Dataset Preview
</h3>


<p align="left">

<img src="./img/dataset10.webp" width="700">

</p>


<hr>


<h2>🧠 Machine Learning Model</h2>


<h3>Random Forest Classifier</h3>


<p>
Random Forest Classifier is used to classify wines into quality categories
based on their chemical properties.
</p>


<p>
The model creates multiple decision trees and combines their predictions to
achieve better accuracy.
</p>


<pre>

Input:

Alcohol = 12%
pH = 3.3
Acidity = Normal


Output:

Quality = High

</pre>


<hr>


<h2>❓ Why This Model?</h2>


<ul>

<li>Wine quality depends on multiple chemical factors.</li>

<li>The relationship between features and quality is nonlinear.</li>

<li>Random Forest handles complex datasets effectively.</li>

<li>It reduces overfitting using multiple trees.</li>

<li>It provides feature importance analysis.</li>

</ul>


<hr>


<h2>🧮 Mathematical Explanation</h2>


<p>
Random Forest consists of multiple Decision Trees.
Each tree predicts a class and the final result is selected by voting.
</p>


<p align="center">

<b>
Prediction = Majority Vote(Tree₁, Tree₂, ... , Treeₙ)
</b>

</p>


<h3>Decision Tree Split</h3>


<p>
Trees select the best feature split using impurity measurement.
</p>


<h3>Gini Impurity</h3>


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
The algorithm selects splits that create more pure groups of wine quality.
</p>


<hr>


<h2>⚙ Model Learning Process</h2>


<ul>

<li>Create multiple random samples from dataset</li>

<li>Build decision trees</li>

<li>Train each tree with different data</li>

<li>Collect predictions from all trees</li>

<li>Select final quality prediction</li>

</ul>


<hr>


<h2>📈 Model Evaluation</h2>


<h3>Accuracy</h3>

<p>
Measures how many wine samples were classified correctly.
</p>


<p align="center">

<b>
Accuracy = Correct Predictions / Total Predictions
</b>

</p>


<h3>Precision</h3>

<p>
Shows how many predicted quality classes were correct.
</p>


<h3>Recall</h3>

<p>
Shows how many real quality classes were detected.
</p>


<h3>F1 Score</h3>

<p>
Balances precision and recall.
</p>


<h3>Confusion Matrix</h3>

<p>
Shows classification performance between different quality levels.
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

Wine-Quality-Prediction
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

<li>Compare different Machine Learning algorithms</li>

<li>Use XGBoost and Gradient Boosting</li>

<li>Apply regression models for exact quality scores</li>

<li>Create wine recommendation system</li>

<li>Deploy as a quality prediction application</li>

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