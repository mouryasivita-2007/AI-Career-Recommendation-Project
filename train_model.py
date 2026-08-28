import numpy as np
import pandas as pd

# Split data into training and testing
from sklearn.model_selection import train_test_split

# RandomForestDecision Tree ML model
from sklearn.ensemble import RandomForestClassifier

# Check model accuracy
from sklearn.metrics import accuracy_score

# Saved the trained model
import joblib


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

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train the model
model.fit(X_train, y_train)


# Predict test data
preds = model.predict(X_test)

# Check accuracy
print("Accuracy:", accuracy_score(y_test, preds))


# Save the trained model
joblib.dump(model,'career_model.pkl')

print("Model Saved Successfully")