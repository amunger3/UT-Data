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

# Scatterplot of weight vs. mpg
fig, ax = plt.subplots()
ax.scatter(cars_df['wt'], cars_df['mpg'])

ax.set_xlabel('Weight')
ax.set_ylabel('MPG')
ax.set_title('Weight vs. MPG')

ax.grid(True)
plt.show()

# Boxplot of mpg by cylinder count
fig, ax = plt.subplots()
ax.boxplot([cars_df['mpg'][cars_df['cyl'] == c] for c in sorted(cars_df['cyl'].unique())],
           tick_labels=sorted(cars_df['cyl'].unique()))

ax.set_xlabel('Cylinder Count')
ax.set_ylabel('MPG')
ax.set_title('MPG by Cylinder Count')

plt.show()

# Histogram of horsepower
fig, ax = plt.subplots()
ax.hist(cars_df['hp'], bins=14, color='orange', edgecolor='black')
ax.set_xlabel('Horsepower')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of Horesepower')

plt.show()