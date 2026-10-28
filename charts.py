import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_csv("emp.csv")

#bar chart
avg_salary= df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
bars= plt.bar(avg_salary.index, avg_salary.values)

plt.title("average salary per department")
plt.xlabel("department")
plt.ylabel("avegrage salary")


plt.bar_label(bars, fmt="%.2f")

plt.tight_layout()
plt.savefig("average_salary.png")
plt.show()

#histogram plot

plt.figure(figsize=(8, 5))

plt.hist(df["salary"], bins=5 , edgecolor="black")

plt.title("salary distribution")
plt.xlabel("salary")
plt.ylabel("frequency")


plt.tight_layout()
plt.savefig("salary_histogram.png")
plt.show()

#scatter plot

plt.figure(figsize=(8, 5))

for department in df["department"].unique():
    department_data= df[df["department"]== department]

    plt.scatter(
        department_data["id"],
        department_data["salary"],
        label=department
    )


plt.title("employee id vs salary by department")
plt.xlabel("employee id")
plt.ylabel("salary")
plt.legend(title="department")


plt.tight_layout()
plt.savefig("employee_scatter.png")
plt.show()


#line chart
months= ["jan","feb","mar","apr","may","jun"]
sales= [12,15,14,18,22,25]

plt.figure(figsize=(8, 5))

plt.plot(months,sales,marker="o")

plt.title("montly sales jan - jun")
plt.xlabel("month")
plt.ylabel("sales")


plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()
