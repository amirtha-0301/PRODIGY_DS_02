import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("google_play_store.csv")

# Show basic info
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Clean Rating column
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df = df.dropna(subset=['Rating'])

# Bar Chart: Top 10 App Categories
top_categories = df['Category'].value_counts().head(10)

plt.figure(figsize=(8, 5))
top_categories.plot(kind='bar')
plt.title("Top 10 App Categories on Google Play Store")
plt.xlabel("Category")
plt.ylabel("Number of Apps")
plt.xticks(rotation=45)
plt.show()

# Histogram: App Ratings Distribution
plt.figure(figsize=(8, 5))
plt.hist(df['Rating'], bins=10)
plt.title("Distribution of App Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Apps")
plt.show()

# Bar Chart: Content Rating Distribution
plt.figure(figsize=(6, 4))
df['Content Rating'].value_counts().plot(kind='bar')
plt.title("Content Rating Distribution")
plt.xlabel("Content Rating")
plt.ylabel("Number of Apps")
plt.show()
