# src/analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned CSV
df = pd.read_csv("../data/sp500.csv", index_col=0, parse_dates=True)

# Convert columns to numeric
numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 1️⃣ Daily Returns
df['Daily Return'] = df['Close'].pct_change().fillna(0)

# 2️⃣ Moving Averages
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()

# 3️⃣ Volatility
df['Volatility'] = df['Daily Return'].rolling(window=20).std()

# Plots
plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Close')
plt.plot(df['MA20'], label='20-Day MA')
plt.plot(df['MA50'], label='50-Day MA')
plt.title("S&P 500 Closing Price & Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

plt.figure(figsize=(12,6))
plt.plot(df['Volatility'], color='orange')
plt.title("S&P 500 20-Day Rolling Volatility")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.show()
