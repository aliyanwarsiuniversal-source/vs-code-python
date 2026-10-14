import pandas as pd

# 1. Create a dictionary with sample data
data = {
    'Name': ['Aliyan', 'Ahmed', 'Sara'],
    'Age': [16, 22, 21],
    'Score': [100, 90, 88]
}

# 2. Convert dictionary into a Pandas DataFrame (Table)
df = pd.DataFrame(data)

# 3. Print the DataFrame
print("--- Student Dataset ---")
print(df)

# 4. Calculate the average score
print("\nAverage Score:", df['Score'].mean())