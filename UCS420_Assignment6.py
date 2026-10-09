#  Lab Assignment 6


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

ROLL_NUMBER = 1024170186
#  Q1
M = float(input("Enter a value for M: "))
x = np.linspace(-10, 10, 400)
y_quadratic = M * x**2
y_sine = M * np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y_quadratic, color="royalblue", linestyle="-", linewidth=2,
         label=r"$y = Mx^2$")
plt.plot(x, y_sine, color="darkorange", linestyle="--", linewidth=2,
         label=r"$y = M\sin(x)$")
plt.title(f"Mathematical Functions for M = {M}")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, linestyle=":")
plt.tight_layout()
plt.show()

 #Q2
subjects = ["Mathematics", "Computer Science", "Physics", "English", "Statistics"]
scores = [85, 92, 78, 88, 81]
score_df = pd.DataFrame({"Subject": subjects, "Score": scores})

plt.figure(figsize=(9, 5))
ax = sns.barplot(data=score_df, x="Subject", y="Score", hue="Subject",
                 palette="Set2", legend=False)
for container in ax.containers:
    ax.bar_label(container, fmt="%.0f", padding=3)
ax.set_title("Scores in Five Subjects")
ax.set_xlabel("Subject")
ax.set_ylabel("Score")
ax.set_ylim(0, max(scores) + 12)
ax.grid(axis="y", linestyle="--", alpha=0.6)
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# Q3
np.random.seed(ROLL_NUMBER)
data = np.random.randn(50)
indices = np.arange(1, len(data) + 1)
cumulative_sum = np.cumsum(data)
random_noise = data + np.random.randn(50) * 0.25

fig, axes = plt.subplots(2, 2, figsize=(12, 8))


axes[0, 0].plot(indices, cumulative_sum, color="teal", marker="o",
                markersize=3, label="Cumulative sum")
axes[0, 0].set_title("Cumulative Sum of 50 Random Values")
axes[0, 0].set_xlabel("Observation")
axes[0, 0].set_ylabel("Cumulative sum")
axes[0, 0].grid(True)
axes[0, 0].legend()

axes[0, 1].scatter(data, random_noise, color="crimson", alpha=0.75)
axes[0, 1].set_title("Scatter Plot with Random Noise")
axes[0, 1].set_xlabel("Original random values")
axes[0, 1].set_ylabel("Values with added noise")
axes[0, 1].grid(True)

axes[1, 0].plot(indices, data, color="slateblue", linestyle="--")
axes[1, 0].set_title("Generated Random Values")
axes[1, 0].set_xlabel("Observation")
axes[1, 0].set_ylabel("Value")
axes[1, 0].grid(True)

sns.histplot(data=data, ax=axes[1, 1], color="seagreen", kde=True)
axes[1, 1].set_title("Distribution of Random Values")
axes[1, 1].set_xlabel("Value")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].grid(True)

fig.suptitle(f"Random Dataset (NumPy seed = {ROLL_NUMBER})", fontsize=14)
fig.tight_layout()
plt.show()

#  Q4
csv_path = "company_sales_data.csv"

try:
    sales_df = pd.read_csv(csv_path)
except FileNotFoundError:
    print(
        "\nQ4 skipped: company_sales_data.csv was not found. "
        "Download the CSV from the GitHub link in the assignment and place it "
        "in the same folder as this script."
    )
else:
    
    normalized_columns = {str(col).strip().lower().replace(" ", "_"): col
                          for col in sales_df.columns}

   
    profit_col = next(
        (original for normalized, original in normalized_columns.items()
         if "total_profit" in normalized or normalized == "profit"),
        None
    )
    month_col = next(
        (original for normalized, original in normalized_columns.items()
         if normalized == "month" or "month_number" in normalized),
        None
    )

    if profit_col is not None:
        plt.figure(figsize=(10, 5))
        if month_col is not None:
            sns.lineplot(data=sales_df, x=month_col, y=profit_col,
                         marker="o", color="purple")
            plt.xlabel("Month")
        else:
            sns.lineplot(data=sales_df, y=profit_col, marker="o", color="purple")
            plt.xlabel("Row")
        plt.title("Total Profit Across Months")
        plt.ylabel("Total Profit")
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()
        plt.show()
    else:
        print("Q4(1): Could not find a total-profit column. Available columns:",
              list(sales_df.columns))

    # 2
    product_cols = [
        original for normalized, original in normalized_columns.items()
        if "product" in normalized and "sales" in normalized
    ]
    if month_col is not None and product_cols:
        plt.figure(figsize=(11, 6))
        for col in product_cols:
            sns.lineplot(data=sales_df, x=month_col, y=col, marker="o", label=str(col))
        plt.title("Monthly Sales for All Products")
        plt.xlabel("Month")
        plt.ylabel("Units Sold")
        plt.legend(title="Product")
        plt.grid(True, linestyle="--", alpha=0.6)
        plt.tight_layout()
        plt.show()
    else:
        print("Q4(2): Could not identify month and product-sales columns.",
              "Available columns:", list(sales_df.columns))

    # 3
    numeric_cols = sales_df.select_dtypes(include="number").columns.tolist()
    if numeric_cols:
        for col in numeric_cols:
            plt.figure(figsize=(10, 5))
            sns.barplot(x=sales_df.index, y=sales_df[col], color="cornflowerblue")
            plt.title(f"Bar Chart: {col}")
            plt.xlabel("Row / Month index")
            plt.ylabel(str(col))
            plt.grid(axis="y", linestyle="--", alpha=0.6)
            plt.tight_layout()
            plt.show()
    else:
        print("Q4(3): No numeric columns were found in the CSV.")
