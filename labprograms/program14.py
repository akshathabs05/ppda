import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("5ds_salaries.csv") 

print("Dataset Preview:")
print(df.head())

plt.figure(figsize=(10, 6))
sns.histplot(df['salary_in_usd'], kde=True, color='skyblue')
plt.title('Salary Distribution (USD)')
plt.xlabel('Salary in USD')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
