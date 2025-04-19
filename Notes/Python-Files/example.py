import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample data
dates = pd.date_range('20230101', periods=100)
df = pd.DataFrame({
    'date': dates,
    'value_a': np.random.randn(100).cumsum(),
    'value_b': np.random.randn(100).cumsum(),
    'category': np.random.choice(['X', 'Y', 'Z'], 100)
})

# Basic data inspection
print("DataFrame head: ")
print(df.head())

print("\nBasic statistics: ")
print(df.describe())

# Data manipulation
# Group by category and calculate mean
grouped = df.groupby('category').mean()
print("\nGrouped by category:")
print(grouped)

# Create a simple line plot
plt.figure(figsize=(10,6))
plt.plot(df['date'], df['value_a'], label='Value A')
plt.plot(df['date'], df['value_b'], label='Value B')
plt.title('Sample Time Series')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save figure
plt.savefig('time_series.png')
