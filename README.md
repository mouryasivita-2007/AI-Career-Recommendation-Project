# AI-Career-Recommendation-Project
AI-based career recommendation system using Machine Learning, Flask, HTML, CSS and JavaScript.
# 🤖 AI Career Recommendation System

A machine-learning-based web application that recommends a career based on a user's skills and interests.

This project started as a simple Python machine learning experiment and was later extended into a complete web application using **Flask, HTML, CSS and JavaScript**.

The user rates different skills from **1 to 5**, and the trained ML model predicts the most suitable career along with the probability distribution for the available career options.

---

## ✨ Features

* AI/ML-based career recommendation
* 10 skill and interest inputs
* Interactive 1–5 sliders
* Random Forest classification model
* Career prediction using `model.predict()`
* Career probabilities using `model.predict_proba()`
* Flask backend and REST-style `/predict` endpoint
* JavaScript Fetch API for frontend-backend communication
* JSON data exchange
* Dynamic result display without page refresh
* Probability progress bars
* Responsive web design
* Input values restricted to 1–5

---

## 🎯 Career Options

The model currently works with five career categories:

* Software Developer
* Data Scientist
* Cybersecurity Analyst
* Business Analyst
* UI/UX Designer

---

## 📊 Input Features

The model uses the following 10 features:

1. Programming
2. Problem Solving
3. Analytical Thinking
4. Mathematics
5. Creativity
6. Communication
7. Design Interest
8. Technical Interest
9. Teamwork
10. Attention to Detail

Each feature is rated from **1 to 5**.

---

## 🧠 Machine Learning

The ML model is trained using a **Random Forest Classifier** from Scikit-learn.

### Training process

```text
Dataset
   ↓
Separate Features and Target
   ↓
Train/Test Split
   ↓
Random Forest Classifier
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Save Trained Model
```

The trained model is saved as:

```text
career_model.pkl
```

The model is then loaded by Flask when the web application starts.

---

## 🌐 How the Web Application Works

The application has three main layers:

### Frontend

Built using:

* HTML
* CSS
* JavaScript

The HTML page provides the career assessment form, while CSS handles the design and JavaScript handles user interaction.

### Backend

Built using:

* Python
* Flask

Flask receives the user's ratings and passes them to the trained ML model.

### Machine Learning

The trained Random Forest model predicts:

* Recommended career
* Probability for each career

---

## 🔄 Complete Project Flow

```text
User
 ↓
HTML Sliders
 ↓
JavaScript collects values
 ↓
fetch("/predict")
 ↓
POST request with JSON
 ↓
Flask API
 ↓
request.json
 ↓
Pandas DataFrame
 ↓
Random Forest Model
 ↓
predict()
predict_proba()
 ↓
Flask
 ↓
jsonify()
 ↓
JavaScript receives JSON
 ↓
Dynamic HTML update
 ↓
Career + Probability Bars
```

---

## 🔗 Important Connections

### HTML → CSS

```html
<link rel="stylesheet"
      href="{{ url_for('static', filename='style.css') }}">
```

Connects the webpage with its styling.

### HTML → JavaScript

```html
<script src="{{ url_for('static', filename='script.js') }}"></script>
```

Loads the JavaScript functionality.

### JavaScript → Flask

```javascript
fetch("/predict", {
    method: "POST",
    ...
})
```

Sends the user's ratings to Flask.

### Flask → ML Model

```python
prediction = model.predict(user_data)[0]
```

Gets the recommended career.

### Flask → ML Probabilities

```python
probabilities = model.predict_proba(user_data)[0]
```

Gets the model's probability distribution.

### Flask → JavaScript

```python
return jsonify({
    "career": prediction,
    "probabilities": probability_data
})
```

Sends the prediction back to the browser.

### JavaScript → HTML

```javascript
result.innerHTML = `...`;
```

Dynamically displays the result on the webpage.

---

## 📁 Project Structure

```text
AI-Career-Recommendation/
│
├── app.py
├── train_model.py
├── ai_career_recommendation_dataset.csv
├── career_model.pkl
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js


### File Purpose

| File                                   | Purpose                                  |
| -------------------------------------- | ---------------------------------------- |
| `train_model.py`                       | Trains and saves the ML model            |
| `career_model.pkl`                     | Saved Random Forest model                |
| `app.py`                               | Flask server and prediction API          |
| `index.html`                           | Website structure                        |
| `style.css`                            | Website styling                          |
| `script.js`                            | Slider interaction and API communication |
| `ai_career_recommendation_dataset.csv` | Training dataset                         |

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Flask
* HTML5
* CSS3
* JavaScript
* Fetch API
* JSON

---

## ▶️ Running the Project

Install the required libraries:

```bash
pip install pandas numpy scikit-learn flask joblib
```

First train the model:

```bash
python train_model.py
```

Then start the Flask application:

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000/
```

---

## 💡 Learning Behind the Project

This project helped me understand how different technologies can work together rather than treating Machine Learning and Web Development as completely separate topics.

The final application connects:

```text
Machine Learning
       +
Python
       +
Flask
       +
JavaScript
       +
HTML/CSS
```

The main learning was not just building the prediction model, but understanding how the prediction travels from a user's input on a webpage to the ML model and back to the webpage.

---

## 🚀 Future Improvements

Some possible improvements for future versions:

* Larger and more diverse dataset
* Better model comparison
* Career descriptions and required skills
* Personalized career suggestions
* More career categories
* Improved probability visualization
* User history and saved assessments
* Deployment as an online application

