from flask import Flask,render_template,jsonify,request
import pandas as pd 
import joblib

app = Flask(__name__)

# load the trained ML model
model = joblib.load("career_model.pkl")

features = [
    "Programming",
    "Problem Solving",
    "Analytical Thinking",
    "Mathematics",
    "Creativity",
    "Communication",
    "Design Interest",
    "Technical Interest",
    "Teamwork",
    "Attention to Detail"
]

# home page
@app.route("/")

def home():
    return render_template("index.html")

# prediction API
@app.route("/predict", methods=["POST"])
def predict():

    # Get data sent from JavaScript
    data = request.json

    # Create DataFrame using the same column order as training data
    user_data = pd.DataFrame([[
        data["Programming"],
        data["Problem Solving"],
        data["Analytical Thinking"],
        data["Mathematics"],
        data["Creativity"],
        data["Communication"],
        data["Design Interest"],
        data["Technical Interest"],
        data["Teamwork"],
        data["Attention to Detail"]
    ]], columns=features)

    # Predict career
    prediction = model.predict(user_data)[0]

    # Get probabilities
    probabilities = model.predict_proba(user_data)[0]

    # Create career-probability dictionary
    probability_data = {}
    for career, probability in zip(model.classes_, probabilities):
        probability_data[career] = round(probability * 100, 2)

    # Send result back to JavaScript
    return jsonify({
        "career": prediction,
        "probabilities": probability_data
    })

if __name__ == "__main__":
    app.run(debug=True)
