import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("./data/sp500.csv", index_col=0, parse_dates=True)
    numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df['Daily Return'] = df['Close'].pct_change().fillna(0)
    return df

df = load_data()

# --- Streamlit Layout ---
st.title("📈 Stock Market Trend Analyzer")
st.write("Analyze S&P 500 historical trends, moving averages, daily returns, and volatility.")

# Date range selector
start_date = st.date_input("Start Date", df.index.min())
end_date = st.date_input("End Date", df.index.max())
df_filtered = df[(df.index >= pd.to_datetime(start_date)) & (df.index <= pd.to_datetime(end_date))]

# Moving average selector
ma_window = st.slider("Moving Average Window (days)", min_value=5, max_value=100, value=20)
df_filtered[f"MA{ma_window}"] = df_filtered['Close'].rolling(ma_window).mean()

# Plot Closing Price + MA
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_filtered.index, y=df_filtered['Close'], mode='lines', name='Close'))
fig.add_trace(go.Scatter(x=df_filtered.index, y=df_filtered[f"MA{ma_window}"], mode='lines', name=f'{ma_window}-Day MA'))

# Optional: plot Daily Return
show_return = st.checkbox("Show Daily Returns", value=False)
if show_return:
    fig.add_trace(go.Scatter(x=df_filtered.index, y=df_filtered['Daily Return'], mode='lines', name='Daily Return', yaxis="y2"))

# Layout for second y-axis
fig.update_layout(
    title="S&P 500 Trends",
    xaxis_title="Date",
    yaxis_title="Price",
    yaxis2=dict(
        overlaying='y',
        side='right',
        title='Daily Return',
        showgrid=False
    ),
    legend=dict(x=0, y=1)
)
st.plotly_chart(fig, use_container_width=True)

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df_filtered)
