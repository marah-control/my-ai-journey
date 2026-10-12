# Marah - Control & Automation Engineer
# Day 4: Titanic Data Analysis

import pandas as pd

# 1. Load the data
df = pd.read_csv("train.csv")

print("=== Dataset Shape ===")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\n=== First 5 Rows ===")
print(df.head())

print("\n=== Column Names ===")
print(df.columns.tolist())

print("\n=== Data Types ===")
print(df.dtypes)

print("\n=== Missing Values ===")
print(df.isnull().sum())

# 2. Survival Analysis
print("\n=== Survival Count ===")
print(df["Survived"].value_counts())

print("\n=== Survival Rate ===")
print(f"{df['Survived'].mean() * 100:.2f}%")

# 3. Survival by Gender
print("\n=== Survival by Gender ===")
print(df.groupby("Sex")["Survived"].mean())

# 4. Survival by Class
print("\n=== Survival by Passenger Class ===")
print(df.groupby("Pclass")["Survived"].mean())

# 5. Average Age
print("\n=== Average Age ===")
print(f"{df['Age'].mean():.2f} years")

# 6. Age vs Survival
print("\n=== Average Age by Survival ===")
print(df.groupby("Survived")["Age"].mean())
# 7. Visualization
import matplotlib.pyplot as plt

survival_by_sex = df.groupby("Sex")["Survived"].mean()

plt.figure(figsize=(8, 5))
survival_by_sex.plot(kind="bar", color=["pink", "blue"])
plt.title("Survival Rate by Gender")
plt.ylabel("Survival Rate")
plt.xlabel("Gender")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("survival_by_gender.png")
print("\nChart saved as 'survival_by_gender.png'")