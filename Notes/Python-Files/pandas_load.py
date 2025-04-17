import pandas as pd
import numpy as np
# Create a simple DataFrame
def create_sample_dataframe():
    # Sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['New York', 'San Francisco', 'Chicago', 'Boston', 'Seattle'],
        'Salary': [60000, 80000, 70000, 90000, 75000]
    }
    
    # Create DataFrame
    df = pd.DataFrame(data)
    return df
def main():
    # Create the DataFrame
    df = create_sample_dataframe()
    
    # Basic operations
    print("Original DataFrame:")
    print(df)
    
    # Basic statistics
    print("\nBasic Statistics:")
    print(df.describe())

main()