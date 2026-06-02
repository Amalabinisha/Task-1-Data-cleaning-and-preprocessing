import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")

# Explore Dataset

print("First 5 Rows")
print(df.head())

print("\nShape of Dataset")
print(df.shape)

print("\nNumber of Rows :", df.shape[0])
print("Number of Columns :", df.shape[1])

print("\nColumn Names")
print(df.columns)

print("\nData Types")
print(df.dtypes)

# Missing Values Before Handling

print("\nMissing Values in Each Column")
print(df.isnull().sum())

# Missing Value Heatmap BEFORE Handling

plt.figure(figsize=(10,6))

sns.heatmap(df.isnull(),
            yticklabels=False,
            cbar=True,
            cmap='viridis')

plt.title("Missing Values Before Handling")

plt.show()

# Handling Missing Values

df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

df['Cabin'] = df['Cabin'].fillna("Unknown")

# Missing Values After Handling

print("\nMissing Values After Handling")
print(df.isnull().sum())

# Heatmap After Handling

plt.figure(figsize=(10,6))

sns.heatmap(df.isnull(),
            yticklabels=False,
            cbar=True,
            cmap='viridis')

plt.title("Missing Values After Handling")

plt.show()

# Data Type Conversion

df['Survived'] = df['Survived'].astype('category')

df['Pclass'] = df['Pclass'].astype('category')

print("\nUpdated Data Types")
print(df.dtypes)

# Target Variable Analysis

print("\nTarget Variable Distribution")
print(df['Survived'].value_counts())

# Class Imbalance Percentage

class_percentage = df['Survived'].value_counts(normalize=True) * 100

print("\nClass Percentage")
print(class_percentage)

# Count Plot

plt.figure(figsize=(6,5))

sns.countplot(x='Survived', data=df)

plt.title("Distribution of Target Variable")

plt.xlabel("Survived")

plt.ylabel("Count")

plt.show()

# Pie Chart

plt.figure(figsize=(6,6))

df['Survived'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Class Imbalance")

plt.ylabel("")

plt.show()

# Save Cleaned Dataset

df.to_csv("Cleaned_Titanic_Dataset.csv", index=False)

print("\nCleaned Dataset Saved Successfully")