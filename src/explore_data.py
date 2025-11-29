# src/explore_data.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("../data/sp500.csv", index_col=0, parse_dates=True)

# Convert columns to numeric (in case they were read as objects)
numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Check for missing values
print("Missing values:\n", df.isnull().sum())

# Quick overview
print("\nHead of the data:")
print(df.head())

print("\nSummary statistics:")
print(df.describe())

# Plot the closing price
plt.figure(figsize=(12,6))
plt.plot(df['Close'])
plt.title("S&P 500 Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
