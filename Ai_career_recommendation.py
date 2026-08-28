import numpy as np
import pandas as pd

# Split data into training and testing
from sklearn.model_selection import train_test_split

# Decision Tree ML model
from sklearn.tree import DecisionTreeClassifier

# Check model accuracy
from sklearn.metrics import accuracy_score


# Read the CSV dataset
df = pd.read_csv('ai_career_recommendation_dataset.csv')

# Display first 5 rows
print(df.head(5))


# Input features
X = df.drop('Career', axis=1)

# Target career
y = df['Career']


# Split data: 80% train and 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)


# Predict test data
preds = model.predict(X_test)

# Check accuracy
print("Accuracy:", accuracy_score(y_test, preds))


# Take input from user
print("\nEnter your details:")


# Allow ratings only from 1 to 5
def get_rating(feature):
    while True:
        try:
            value = float(input(f"{feature} (1-5): "))

            if 1 <= value <= 5:
                return value

            print("Please enter a value between 1 and 5.")

        except ValueError:
            print("Please enter a valid number.")


# Get user ratings
programming = get_rating("Programming")
problem_solving = get_rating("Problem Solving")
analytical_thinking = get_rating("Analytical Thinking")
mathematics = get_rating("Mathematics")
creativity = get_rating("Creativity")
communication = get_rating("Communication")
design_interest = get_rating("Design Interest")
technical_interest = get_rating("Technical Interest")
teamwork = get_rating("Teamwork")
attention_to_detail = get_rating("Attention to Detail")


# Create DataFrame for user input
user_data = pd.DataFrame([[
    programming,
    problem_solving,
    analytical_thinking,
    mathematics,
    creativity,
    communication,
    design_interest,
    technical_interest,
    teamwork,
    attention_to_detail
]], columns=X.columns)

print("")
# Get prediction probabilities
probabilities = model.predict_proba(user_data)

# Get career names
careers = model.classes_


# Display probabilities
for career, probability in zip(careers, probabilities[0]):
    print(career, ":", round(probability * 100, 2), "%")


# Get final career prediction
result = model.predict(user_data)

print("\nRecommended Career:", result[0])