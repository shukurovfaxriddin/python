# dataframe 1

import pandas as pd

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
df1
# Task 1 

df1["Average"] = df1[["Math", "English", "Science"]].mean(axis=1)
print(df1)



# Task 2

top_student = df1.loc[df1["Average"].idxmax()]
print(top_student)


# task 3

df1["Total"] = df1[["Math", "English", "Science"]].sum(axis=1)
print(df1)

# Task 4
import matplotlib.pyplot as plt

subject_averages = df1[["Math", "English", "Science"]].mean()

subject_averages.plot(kind="bar", color=["skyblue", "salmon", "lightgreen"])
plt.title("Average Grades per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Grade")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Dataframe 2

import pandas as pd

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
# task 2

total_sales = df2[["Product_A", "Product_B", "Product_C"]].sum()
print(total_sales)

# Task 2
df2["Total_Sales"] = df2[["Product_A", "Product_B", "Product_C"]].sum(axis=1)
max_sales_date = df2.loc[df2["Total_Sales"].idxmax(), "Date"]
print("Date with highest total sales:", max_sales_date)

# task 3

percentage_change = df2[["Product_A", "Product_B", "Product_C"]].pct_change() * 100
print(percentage_change)

# Task 4

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(df2["Date"], df2["Product_A"], label="Product A", marker="o")
plt.plot(df2["Date"], df2["Product_B"], label="Product B", marker="o")
plt.plot(df2["Date"], df2["Product_C"], label="Product C", marker="o")

plt.title("Sales Trends for Products Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# dataframe 3

import pandas as pd

data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)
df3
# Task 1

avg_salary = df3.groupby("Department")["Salary"].mean()
print(avg_salary)

# task 2

most_experienced = df3.loc[df3["Experience (Years)"].idxmax()]
print(most_experienced)

# task 3

min_salary = df3["Salary"].min()
df3["Salary Increase (%)"] = ((df3["Salary"] - min_salary) / min_salary) * 100
print(df3)

# Task 4

import matplotlib.pyplot as plt

department_counts = df3["Department"].value_counts()

department_counts.plot(kind="bar", color="skyblue")
plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# dataframe 4

import pandas as pd

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
df4
# task 1

total_revenue = df4["Total_Price"].sum()
print("Total Revenue:", total_revenue)

# Task 2

most_ordered = df4.groupby("Product")["Quantity"].sum().idxmax()
print("Most Ordered Product:", most_ordered)

# Task 3

average_quantity = df4["Quantity"].mean()
print("Average Quantity Ordered:", average_quantity)

# Task 4

import matplotlib.pyplot as plt

sales_by_product = df4.groupby("Product")["Total_Price"].sum()

sales_by_product.plot(kind="pie", autopct="%1.1f%%", startangle=140, colors=["#66b3ff", "#99ff99", "#ff9999"])
plt.title("Sales Distribution by Product")
plt.ylabel("")  # Hide y-axis label
plt.tight_layout()
plt.show()
