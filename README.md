#  AI Career Recommendation System

An AI-powered web application that analyzes user skills and interests to suggest the **Top 3 suitable career paths** using Machine Learning.

 Live Demo: (Add your deployed link here)  
Repository: https://github.com/Amrutanshu-07/AI-Career-Recommendation-System

---

##  Project Overview

Choosing the right career path can be challenging. This system provides intelligent career suggestions by:

- Taking user **skills** and **interests** as input
- Processing them using NLP techniques
- Predicting top 3 matching careers
- Displaying confidence scores with dynamic UI

The system uses a supervised machine learning pipeline built with Scikit-learn and deployed using Flask.

---

##  Problem Statement

**Input:**  
- Skills (e.g., Python, Data Analysis, Marketing)  
- Interests (e.g., AI, Healthcare, Business)

**Output:**  
- Top 3 recommended career paths  
- Confidence percentage for each suggestion  

---

##  Machine Learning Approach

### 1️ Data Preprocessing
- Skills and Interests are merged into a single text feature
- Text cleaned and transformed using **TF-IDF Vectorization**

### 2️ Feature Engineering
- `TfidfVectorizer(stop_words="english")`
- Converts text into numerical feature vectors

### 3️ Model Used
- **Logistic Regression (Multiclass)**
- Chosen because:
  - Efficient for text classification
  - Handles sparse TF-IDF vectors well
  - Produces probability outputs
  - Simple and interpretable

### 4️ Model Pipeline

```python
Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000))
])
Dataset

15 Career Categories

8 Samples per Career

Total: 120 samples

Balanced dataset

Stratified train-test split used

Example:

Skills	Interests	Career
python machine learning	ai research	Data Scientist
java spring boot	backend systems	Software Engineer
biology anatomy	healthcare	Doctor

 Web Application Flow
User Input (Skills + Interests)
        ↓
Flask Backend
        ↓
Trained ML Model
        ↓
Top 3 Career Predictions
        ↓
Dynamic UI with Progress Bars
 UI Features

Modern gradient background

Card-based layout

Animated progress bars

Responsive design

Clean professional interface

 Installation & Setup
1️Clone Repository
git clone https://github.com/Amrutanshu-07/AI-Career-Recommendation-System.git
cd AI-Career-Recommendation-System
2️ Install Dependencies
pip install -r requirements.txt
3️ Train Model (If Needed)

Open Jupyter Notebook:

jupyter notebook

Run:

model/train_model.ipynb
4️ Run Application
python app.py

Open in browser:

http://127.0.0.1:5000
 Deployment

This project is deployment-ready using:

Render

Railway

Heroku

AWS EC2

Docker

Deployment files included:

Procfile

runtime.txt

requirements.txt

gunicorn configuration

 Evaluation Metrics

Stratified train-test split

Multiclass classification

Accuracy

Precision

Recall

F1-Score

 Future Improvements

Resume (PDF) based prediction

Deep learning embeddings (BERT)

Career skill gap analysis

Database integration

REST API endpoint

Dashboard analytics

User authentication system
