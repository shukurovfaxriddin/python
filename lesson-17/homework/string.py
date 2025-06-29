import pandas as pd
import numpy as np

# 1. Original Data
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# 2. Rename column names using a function
df.rename(columns=lambda x: x.lower().replace(' ', '_'), inplace=True)

# 3. Print the first 3 rows of the DataFrame
print("First 3 rows:\n", df.head(3))

# 4. Find the mean age
mean_age = df['age'].mean()
print("\nMean Age:", mean_age)

# 5. Select and print only the 'first_name' and 'city' columns
print("\nName and City columns:\n", df[['first_name', 'city']])

# 6. Add a new column 'Salary' with random salary values
np.random.seed(42)  # For reproducibility
df['salary'] = np.random.randint(50000, 100000, size=len(df))

# 7. Display summary statistics
print("\nSummary Statistics:\n", df.describe(include='all'))
import pandas as pd

# 1. Create the DataFrame
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)

# 2. Calculate and display maximum sales and expenses
max_sales = sales_and_expenses['Sales'].max()
max_expenses = sales_and_expenses['Expenses'].max()
print("Maximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)

# 3. Calculate and display minimum sales and expenses
min_sales = sales_and_expenses['Sales'].min()
min_expenses = sales_and_expenses['Expenses'].min()
print("\nMinimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

# 4. Calculate and display average sales and expenses
avg_sales = sales_and_expenses['Sales'].mean()
avg_expenses = sales_and_expenses['Expenses'].mean()
print("\nAverage Sales:", avg_sales)
print("Average Expenses:", avg_expenses)
import pandas as pd

# 1. Create the DataFrame
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

# 2. Set 'Category' as the index
expenses = expenses.set_index('Category')

# 3. Maximum expense for each category
max_expenses = expenses.max(axis=1)
print("Maximum expense for each category:\n", max_expenses)

# 4. Minimum expense for each category
min_expenses = expenses.min(axis=1)
print("\nMinimum expense for each category:\n", min_expenses)

# 5. Average expense for each category
avg_expenses = expenses.mean(axis=1)
print("\nAverage expense for each category:\n", avg_expenses)
