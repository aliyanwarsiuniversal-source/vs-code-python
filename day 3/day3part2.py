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
# Task 4: Scatter Plot using Seaborn
sns.scatterplot(x='Age', y='Score', data=df1, hue='Name', s=100)
plt.title('Age vs Score Analysis')
plt.xlabel('Age')
plt.ylabel('Score')
plt.show()
