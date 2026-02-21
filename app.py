from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/saved_model.pkl")

def suggest_career(skills, interests):
    user_input = skills.lower() + " " + interests.lower()
    probabilities = model.predict_proba([user_input])[0]
    careers = model.classes_
    top_indices = probabilities.argsort()[-3:][::-1]
    return [(careers[i], round(probabilities[i]*100, 2)) for i in top_indices]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        skills = request.form["skills"]
        interests = request.form["interests"]
        results = suggest_career(skills, interests)
        return render_template("result.html", results=results)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()