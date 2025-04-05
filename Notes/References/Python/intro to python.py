import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create sample data
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Sales': [250000, 300000, 280000, 325000, 390000],
    'Expenses': [225000, 250000, 270000, 280000, 300000],
    'Profit': [25000, 50000, 10000, 45000, 90000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Basic DataFrame operations
print("DataFrame:")
print(df)
print("\nBasic Stats:")
print(df.describe())

# Calculate profit margin
df['Profit_Margin'] = df['Profit'] / df['Sales'] * 100
print("\nDataFrame with Profit Margin:")
print(df)

# Filter data
print("\nYears with Profit > 40000:")
print(df[df['Profit'] > 40000])

# Grouping and aggregation
print("\nAverage values by year > 2020:")
print(df[df['Year'] > 2020].mean())

# Data visualization
# Create a figure with multiple subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Line plot for financial trends
ax1.plot(df['Year'], df['Sales'], marker='o', linewidth=2, label='Sales')
ax1.plot(df['Year'], df['Expenses'], marker='s', linewidth=2, label='Expenses')
ax1.plot(df['Year'], df['Profit'], marker='^', linewidth=2, label='Profit')
ax1.set_title('Financial Trends 2018-2022')
ax1.set_xlabel('Year')
ax1.set_ylabel('Amount ($)')
ax1.legend()
ax1.grid(True)

# Bar chart for profit margin
bars = ax2.bar(df['Year'], df['Profit_Margin'], color='teal')
ax2.set_title('Profit Margin by Year')
ax2.set_xlabel('Year')
ax2.set_ylabel('Profit Margin (%)')
ax2.set_ylim(0, 25)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{height:.1f}%', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Another visualization example: scatter plot with size representing profit
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['Sales'], s=df['Profit']/1000, alpha=0.7, 
            c=df['Profit_Margin'], cmap='viridis')
plt.colorbar(label='Profit Margin (%)')
plt.title('Sales vs Year (size represents profit)')
plt.xlabel('Year')
plt.ylabel('Sales ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
