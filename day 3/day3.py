import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "Name": ["Aliyan", "Aijaz", "Hamza", "Sara"],
    "Score": [85, 92, 78, 88],
    "Age": [15, 40, 16, 14]
}

df1 = pd.DataFrame(data)

# Task 3: Line Plot
plt.plot(df1["Name"], df1["Age"], marker="o")
plt.title("Age Distribution")
plt.xlabel("Name")
plt.ylabel("Age")
plt.show()