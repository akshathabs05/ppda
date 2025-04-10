import pandas as pd

# Load the CSV file
file_path = input("Enter the CSV file path: ")
df = pd.read_csv(file_path)

# Display the last 3 rows
print("\nLast 3 Rows:")
print(df.tail(3))

# Display DataFrame description and information
print("\nDataFrame Description:")
print(df.describe())  # Statistical summary

print("\nDataFrame Information:")
print(df.info())  # Data types and memory usage

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())
