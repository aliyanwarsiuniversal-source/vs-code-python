import numpy as np
import pandas as pd

# ==========================================
# Task 1: Handling Missing Data (NaN Values)
# ==========================================

data = {
    "Name": ["Aliyan", "Sara", "Umer", "Zara", "Ahmed"],
    "Age": [22, np.nan, 25, 21, np.nan],
    "Score": [85, 76, np.nan, 88, 79],
}

df1 = pd.DataFrame(data)

# Check missing values
print("--- Missing Values Count ---")
print(df1.isnull().sum())

# Fill missing Age with mean age
mean_age = df1["Age"].mean()
df1["Age"] = df1["Age"].fillna(mean_age)

# Drop rows with missing Score
df1 = df1.dropna(subset=["Score"])

print("\n--- Cleaned DataFrame (Task 1) ---")
print(df1)

# Task 2 data inspiction

print("\n--- 1. Basic Info ---")
df1.info()

print("\n--- 2. Missing Values Count ---")
print(df1.isnull().sum())

print("\n--- 3. Duplicate Rows Count ---")
print(df1.duplicated().sum())

#task 3 data cleaning
# --- TASK 3: DATA CLEANING ---

# 1. Fill missing values (NaN) with the mean (average) of the column
df1['Age'] = df1['Age'].fillna(df1['Age'].mean())
df1['Score'] = df1['Score'].fillna(df1['Score'].mean())

# 2. Remove duplicate rows from the dataset
df1 = df1.drop_duplicates()

# Display the cleaned DataFrame
print("\n--- Cleaned DataFrame (Task 3) ---")
print(df1)
# --- TASK 4: FILTERING & SUMMARY STATISTICS ---                                                                               cr7

# 1. Filter rows where Score is greater than 80 oh yes
high_scorers = df1[df1['Score'] > 80]
print("\n--- High Scorers (Score > 80) ---")
print(high_scorers) 

# 2. Get overall summary statistics of the numerical columns
print("\n--- Summary Statistics ---")
print(df1.describe())