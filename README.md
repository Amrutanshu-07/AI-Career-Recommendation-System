### AI Career Recommendation System

An AI-powered web application that analyzes user skills and interests to recommend the Top 3 suitable career paths using Machine Learning.


 ### Project Overview

Choosing the right career path can be challenging. This system provides intelligent career suggestions by:

Accepting user skills and interests

Processing them using Natural Language Processing (NLP)

Predicting the top 3 matching careers

Displaying confidence scores with a dynamic web interface

The system uses a supervised machine learning pipeline built with Scikit-learn and deployed using Flask.

### Problem Statement

Input:

Skills (e.g., Python, Data Analysis, Marketing)

Interests (e.g., AI, Healthcare, Business)

Output:

Top 3 recommended career paths

### Confidence percentage for each suggestion

 Machine Learning Approach
1️Data Preprocessing

Skills and interests are merged into a single text feature

Text is transformed using TF-IDF Vectorization

df["text"] = df["skills"] + " " + df["interests"]
2️ Feature Engineering

We use:

TfidfVectorizer(stop_words="english")

Why TF-IDF?

Converts text into numerical vectors

Highlights important words

Removes common stop words

Efficient for text classification

3️ Model Used

Logistic Regression (Multiclass)

LogisticRegression(max_iter=1000)
Why Logistic Regression?

Works well for multiclass classification

Handles sparse TF-IDF vectors efficiently

Provides probability outputs

Simple and interpretable

Fast training

4️ML Pipeline
Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000))
])

### This ensures:

Clean modular workflow

Automatic preprocessing + classification

Easy saving and deployment

### Dataset Information

15 Career Categories

8 Samples per Career

Total: 120 records

Balanced dataset

Stratified train-test split

Example Dataset Entries
Skills	Interests	Career
python machine learning	ai research	Data Scientist
java spring boot	backend systems	Software Engineer
biology anatomy	healthcare	Doctor

### Project Structure

 Application Workflow
User Input (Skills + Interests)
        ↓
Flask Backend
        ↓
Trained ML Model
        ↓
Top 3 Career Predictions
        ↓
Dynamic UI with Confidence Bars
 ### User Interface Features

Modern gradient background

Card-based centered layout

Animated progress bars

Responsive design

Professional academic UI

 ### Installation & Setup
1️ Clone Repository
git clone https://github.com/Amrutanshu-07/AI-Career-Recommendation-System.git
cd AI-Career-Recommendation-System
2️ Install Dependencies
pip install -r requirements.txt
3️ Train Model (If Required)
jupyter notebook

Run:

model/train_model.ipynb
4️ Run Application
python app.py

Open in browser:

http://127.0.0.1:5000
 Deployment


