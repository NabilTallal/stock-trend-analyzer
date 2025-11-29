# src/dashboard_plotly.py
import pandas as pd
import plotly.graph_objects as go

# Load CSV
df = pd.read_csv("../data/sp500.csv", index_col=0, parse_dates=True)
numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Calculate moving averages
df['MA20'] = df['Close'].rolling(20).mean()
df['MA50'] = df['Close'].rolling(50).mean()

# Interactive plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['Close'], mode='lines', name='Close'))
fig.add_trace(go.Scatter(x=df.index, y=df['MA20'], mode='lines', name='20-Day MA'))
fig.add_trace(go.Scatter(x=df.index, y=df['MA50'], mode='lines', name='50-Day MA'))

fig.update_layout(title="S&P 500 Closing Price & Moving Averages",
                  xaxis_title="Date", yaxis_title="Price")
fig.show()