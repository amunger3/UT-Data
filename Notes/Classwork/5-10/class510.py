import pandas as pd


data = { 
        'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 34, 29, 42],
        'City': ['New York', 'Boston', 'Chicago', 'Seattle'],
        'Salary': [65000, 72000, 67000, 85000]
        } 

df = pd.DataFrame(data)
print(df)