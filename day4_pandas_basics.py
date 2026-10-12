# Marah - Control & Automation Engineer
# Day 4: Pandas Basics

import pandas as pd

# 1. Create a simple DataFrame
data = {
    "name": ["Ali", "Sara", "Omar", "Lina", "Hadi"],
    "age": [22, 24, 23, 21, 25],
    "grade": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("=== Full DataFrame ===")
print(df)

print("\n=== First 3 rows ===")
print(df.head(3))

print("\n=== Data Info ===")
print(df.info())

print("\n=== Statistics ===")
print(df.describe())

print("\n=== Average Grade ===")
print(df["grade"].mean())

print("\n=== Students with grade > 85 ===")
print(df[df["grade"] > 85])