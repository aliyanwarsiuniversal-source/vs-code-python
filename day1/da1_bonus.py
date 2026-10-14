import pandas as pd

# 1. Sample grocery data
data = {
    'Item': ['Apple', 'Milk', 'Bread'],
    'Price': [120, 170, 140],
    'Quantity': [2, 3, 1]
}

# 2. Create DataFrame
df = pd.DataFrame(data)

# 3. Calculate total for each item (Price * Quantity)
df['Total'] = df['Price'] * df['Quantity']

print("--- Grocery Bill ---")
print(df)

# 4. Calculate overall grand total
grand_total = df['Total'].sum()
print("\nGrand Total Bill:", grand_total)