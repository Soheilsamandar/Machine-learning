<h1 align="center">🎬 Movie Recommendation System</h1>

<h3 align="center">
Machine Learning Recommendation System Project for Suggesting Movies to Users
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
Movie Recommendation System is a Machine Learning project that suggests movies
to users based on their interests, previous ratings, and similarity between
movies.
</p>

<p>
The goal of this project is to build an intelligent system that can understand
user preferences and recommend movies that the user is likely to enjoy.
</p>

<p>
Recommendation systems are widely used in platforms such as Netflix, YouTube,
Spotify, and Amazon to personalize user experiences.
</p>


<hr>


<h2>🎯 What We Are Going To Do</h2>

<ul>

<li>Analyze movie and user rating data</li>

<li>Understand user preferences</li>

<li>Find similarities between movies</li>

<li>Create a recommendation algorithm</li>

<li>Generate personalized movie suggestions</li>

<li>Evaluate recommendation quality</li>

</ul>


<hr>


<h2>📊 Dataset</h2>

<p>
The dataset contains information about movies, users, and their ratings.
Each row represents a user's interaction with a movie.
</p>


<table border="1">

<tr>
<th>Feature</th>
<th>Description</th>
</tr>


<tr>
<td>User ID</td>
<td>Unique identifier for each user</td>
</tr>


<tr>
<td>Movie ID</td>
<td>Unique identifier for each movie</td>
</tr>


<tr>
<td>Movie Title</td>
<td>Name of the movie</td>
</tr>


<tr>
<td>Genre</td>
<td>Movie category</td>
</tr>


<tr>
<td>Rating</td>
<td>User rating score</td>
</tr>


<tr>
<td>Timestamp</td>
<td>Date of interaction</td>
</tr>


</table>


<h3 align="left">
Dataset Preview
</h3>


<p align="left">

<img src="./img/dataset11.webp" width="700">

</p>


<hr>


<h2>🧠 Machine Learning Model</h2>


<h3>Collaborative Filtering</h3>


<p>
Collaborative Filtering is used to recommend movies by analyzing similarities
between users and movies.
</p>


<p>
The system assumes that users with similar interests will probably like similar
movies in the future.
</p>


<pre>

Example:

User A likes:
- Interstellar
- Inception
- Matrix


User B likes:
- Interstellar
- Inception


Recommendation:

Suggest Matrix to User B

</pre>


<hr>


<h2>❓ Why This Model?</h2>


<ul>

<li>Recommendations depend on user behavior.</li>

<li>The system learns from previous ratings.</li>

<li>It does not require manually defining movie rules.</li>

<li>It can discover hidden relationships between users and movies.</li>

<li>It is widely used in real-world recommendation platforms.</li>

</ul>


<hr>


<h2>🧮 Mathematical Explanation</h2>


<p>
Collaborative Filtering uses similarity calculations to find relationships
between users or movies.
</p>


<h3>Cosine Similarity</h3>


<p align="center">

<b>
Similarity(A,B) =
(A · B) / (||A|| × ||B||)
</b>

</p>


<table border="1">

<tr>
<th>Symbol</th>
<th>Meaning</th>
</tr>


<tr>
<td>A · B</td>
<td>Dot product between vectors</td>
</tr>


<tr>
<td>||A||</td>
<td>Magnitude of vector A</td>
</tr>


<tr>
<td>||B||</td>
<td>Magnitude of vector B</td>
</tr>


</table>


<p>
The higher the similarity value, the more similar two users or movies are.
</p>


<hr>


<h2>⚙ Model Learning Process</h2>


<ul>

<li>Create user-movie rating matrix</li>

<li>Convert users and movies into numerical vectors</li>

<li>Calculate similarity between items</li>

<li>Find similar movies or users</li>

<li>Generate recommendations</li>

</ul>


<h3>User-Movie Matrix</h3>


<pre>

          Movie1  Movie2  Movie3

User1       5       4       0

User2       5       0       3

User3       0       4       5

</pre>


<p>
The model learns hidden patterns from this matrix.
</p>


<hr>


<h2>📈 Model Evaluation</h2>


<h3>RMSE (Root Mean Squared Error)</h3>

<p>
Measures the difference between predicted ratings and real ratings.
</p>


<p align="center">

<b>
RMSE = √((1/n)Σ(y - ŷ)²)
</b>

</p>


<h3>MAE (Mean Absolute Error)</h3>

<p>
Shows average recommendation prediction error.
</p>


<p align="center">

<b>
MAE = (1/n)Σ|y - ŷ|
</b>

</p>


<h3>Precision@K</h3>

<p>
Measures how many recommended movies are actually relevant for users.
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

Movie-Recommendation-System
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

<li>Use Deep Learning Recommendation Models</li>

<li>Implement Neural Collaborative Filtering</li>

<li>Add movie posters and descriptions</li>

<li>Create personalized user profiles</li>

<li>Deploy as a web recommendation application</li>

<li>Use real-time recommendation techniques</li>

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