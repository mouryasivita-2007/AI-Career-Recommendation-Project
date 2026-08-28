import pandas as pd
import numpy as np

# Random generator
rng = np.random.default_rng(42)

# Research-informed feature ranges for each career
career_profiles = {

    "Software Developer": {
        "Programming": (4, 5),
        "Problem Solving": (4, 5),
        "Analytical Thinking": (4, 5),
        "Mathematics": (3, 5),
        "Creativity": (3, 5),
        "Communication": (2, 4),
        "Design Interest": (1, 3),
        "Technical Interest": (4, 5),
        "Teamwork": (2, 4),
        "Attention to Detail": (4, 5)
    },

    "Data Scientist": {
        "Programming": (4, 5),
        "Problem Solving": (4, 5),
        "Analytical Thinking": (4, 5),
        "Mathematics": (4, 5),
        "Creativity": (3, 5),
        "Communication": (3, 5),
        "Design Interest": (1, 3),
        "Technical Interest": (4, 5),
        "Teamwork": (2, 4),
        "Attention to Detail": (4, 5)
    },

    "UI/UX Designer": {
        "Programming": (1, 3),
        "Problem Solving": (3, 5),
        "Analytical Thinking": (3, 5),
        "Mathematics": (1, 3),
        "Creativity": (4, 5),
        "Communication": (4, 5),
        "Design Interest": (4, 5),
        "Technical Interest": (3, 5),
        "Teamwork": (3, 5),
        "Attention to Detail": (3, 5)
    },

    "Cybersecurity Analyst": {
        "Programming": (3, 5),
        "Problem Solving": (4, 5),
        "Analytical Thinking": (4, 5),
        "Mathematics": (2, 4),
        "Creativity": (2, 4),
        "Communication": (3, 5),
        "Design Interest": (1, 2),
        "Technical Interest": (4, 5),
        "Teamwork": (2, 4),
        "Attention to Detail": (4, 5)
    },

    "Business Analyst": {
        "Programming": (1, 3),
        "Problem Solving": (4, 5),
        "Analytical Thinking": (4, 5),
        "Mathematics": (2, 4),
        "Creativity": (2, 4),
        "Communication": (4, 5),
        "Design Interest": (1, 3),
        "Technical Interest": (2, 4),
        "Teamwork": (4, 5),
        "Attention to Detail": (4, 5)
    }
}


# Create dataset
rows = []

for career, features in career_profiles.items():

    # 160 records for each career
    for i in range(160):

        row = {}

        for feature, value_range in features.items():

            minimum = value_range[0]
            maximum = value_range[1]

            row[feature] = rng.integers(
                minimum,
                maximum + 1
            )

        row["Career"] = career

        rows.append(row)


# Convert to DataFrame
df = pd.DataFrame(rows)


# Shuffle the dataset
df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)


# Save as CSV
df.to_csv(
    "ai_career_recommendation_dataset.csv",
    index=False
)


# Display information
print("Dataset created successfully!")
print()
print("Rows:", len(df))
print("Columns:", len(df.columns))
print()

print("Career distribution:")
print(df["Career"].value_counts())

print()
print("First 10 records:")
print(df.head(10))