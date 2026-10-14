import pandas as pd

# 1. Sample Data
data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Headphones', 'Laptop', 'Mobile', 'Tablet', 'Headphones'],
    'Sales': [1200, 800, 400, 150, 1400, 950, 500, 200],
    'Region': ['East', 'East', 'East', 'East', 'West', 'West', 'West', 'West'],
    'Discount': [10, 5, 12, 2, 15, 8, 5, 0]
}

# 2. Save Data to CSV
df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False)
print("--- CSV File Created! ---\n")

# 3. Read Data from CSV
loaded_df = pd.read_csv('sales_data.csv')

# 4. Display Data Summary
print("--- First 5 Rows ---")
print(loaded_df.head())

print("\n--- Summary Info ---")
print(loaded_df.info())

import matplotlib.pyplot as plt

# Grouping sales by product
product_sales = loaded_df.groupby('Product')['Sales'].sum()

# Plotting Bar Chart
plt.figure(figsize=(8, 5))
product_sales.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display Chart
plt.show() 

import matplotlib.pyplot as plt

import seaborn as sns

plt.figure(figsize=(8, 5))
sns.boxplot(x='Product', y='Sales', data=loaded_df, palette='Set2')

plt.title('Sales Distribution by Product')
plt.xlabel('Product')
plt.ylabel('Sales ($)')

plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 5))

# Subplot 1: Bar Chart
plt.subplot(1, 2, 1)
product_sales.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales ($)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Subplot 2: Box Plot
plt.subplot(1, 2, 2)
sns.boxplot(x='Product', y='Sales', data=loaded_df, hue='Product', legend=False, palette='Set2')
plt.title('Sales Distribution')
plt.xlabel('Product')
plt.ylabel('Sales ($)')

plt.tight_layout()

#comments for future aliyan warsi
