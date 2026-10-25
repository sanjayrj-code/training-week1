import csv
import matplotlib.pyplot as plt
from collections import defaultdict

# Read employees.csv
ids = []
names = []
departments = []
salaries = []

with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        ids.append(int(row["id"]))
        names.append(row["name"])
        departments.append(row["department"])
        salaries.append(float(row["salary"]))
# Task 1: Bar chart - Average salary per department
department_salaries = defaultdict(list)

for department, salary in zip(departments, salaries):
    department_salaries[department].append(salary)

avg_salary = {
    department: sum(values) / len(values)
    for department, values in department_salaries.items()
}

plt.figure(figsize=(8, 5))
bars = plt.bar(avg_salary.keys(), avg_salary.values())

plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.bar_label(bars, fmt="%.0f")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# Task 2: Histogram - Salary distribution with 5 bins
plt.figure(figsize=(8, 5))

plt.hist(salaries, bins=5, edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig("histogram.png")
plt.show()


# Task 3: Scatter plot - Employee ID vs Salary by department
plt.figure(figsize=(8, 5))

unique_departments = sorted(set(departments))

for department in unique_departments:
    x = [
        ids[i] for i in range(len(ids))
        if departments[i] == department
    ]
    y = [
        salaries[i] for i in range(len(salaries))
        if departments[i] == department
    ]

    plt.scatter(x, y, label=department, s=80)

plt.title("Employee ID vs Salary by Department")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")

plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()


# Task 4: Line chart - Monthly sales from January to June
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

plt.plot(months, sales, marker="o", label="Monthly Sales")

plt.title("Monthly Sales (Jan-Jun)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

print("All four charts saved successfully!")
