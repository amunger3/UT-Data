# imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

cars_df = pd.read_csv('./cars.csv')
# print(cars_df.head())
# print(cars_df.tail())
# print(cars_df.info())
# print(cars_df.describe())

# for r in rows: --> # for [0, 1, 2, 3]
#     for c in cells: # for [0, 1, 2, 3, 4, 5, 6, 7]
#         if c == None: # NoneType is ""
#             print("empty cell")
#   0  1 2 3 4 5 6 7
# 0[x][][][][][][][]
# 1[][y][][][z][][][]
# 2[][][][][a][][c][]
# 3[][][b][][][][][] EOF

print("First 5 rows of the dataset:")
print(cars_df.head())

print("Last 5 rows of the dataset:")
print(cars_df.tail())

print("\nDataset information:")
print(cars_df.info())

print("\nStatistical summary:")
print(cars_df.describe())

# Basic data cleaning
# 1. Check for missing values
print("\nMissing values in each column:")
print(cars_df.isnull().sum())

# 2. Fix column names if necessary (first column appears to have no name):
if '' in cars_df.columns:
    cars = cars_df.rename(columns={'': 'car_name'})

# 3. Convert data types if necessary
numeric_columns = ['mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec']
for col in numeric_columns:
    if col in cars_df.columns:
        cars_df[col] = pd.to_numeric(cars_df[col], errors='coerce')


# Plots
#plt.figure(figsize=(12,8))
#plt.subplot(2, 2, 1)    

# Scatterplot of weight vs. mpg
fig, ax = plt.subplots()
ax.scatter(cars_df['wt'], cars_df['mpg'])

ax.set_xlabel('Weight')
ax.set_ylabel('MPG')
ax.set_title('Weight vs. MPG')

ax.grid(True)
#fig.add_subplot(1, 2, 1)

# Boxplot of mpg by cylinder count
fig, ax = plt.subplots()
ax.boxplot([cars_df['mpg'][cars_df['cyl'] == c] for c in sorted(cars_df['cyl'].unique())],
           tick_labels=sorted(cars_df['cyl'].unique()))

ax.set_xlabel('Cylinder Count')
ax.set_ylabel('MPG')
ax.set_title('MPG by Cylinder Count')

# Histogram of horsepower
fig, ax = plt.subplots()
ax.hist(cars_df['hp'], bins=14, color='orange', edgecolor='black')
ax.set_xlabel('Horsepower')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of Horesepower')

plt.show()

# Claude assisted (from chat)
# # 3. Create a histogram of horsepower
# sns.histplot(df['hp'], kde=True, ax=axes[2], bins=10, color='darkblue', edgecolor='black')
# axes[2].set_title('Distribution of Horsepower', fontsize=14)
# axes[2].set_xlabel('Horsepower', fontsize=12)
# axes[2].set_ylabel('Frequency', fontsize=12)

# # Add summary statistics
# hp_mean = df['hp'].mean()
# hp_median = df['hp'].median()
# axes[2].axvline(hp_mean, color='red', linestyle='--', linewidth=2, label=f'Mean: {hp_mean:.1f}')
# axes[2].axvline(hp_median, color='green', linestyle='-.', linewidth=2, label=f'Median: {hp_median:.1f}')
# axes[2].legend()

# # Adjust layout and display
# plt.tight_layout()
# plt.savefig('car_data_analysis.png', dpi=300)  # Save as high-resolution image
# plt.show()

# # Additional insights table (optional)
# print("\nKey Statistics by Cylinder Count:")
# print(df.groupby('cyl')[['mpg', 'hp', 'wt']].agg(['mean', 'std', 'count']))