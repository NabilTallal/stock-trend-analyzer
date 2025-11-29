# src/fetch_data.py
import yfinance as yf
import pandas as pd


def fetch_sp500_data(symbol="^GSPC", period="5y", interval="1d"):
    """
    Fetch historical S&P 500 data using yfinance and save as CSV.
    """
    print(f"Fetching data for {symbol}...")
    data = yf.download(symbol, period=period, interval=interval)

    # Flatten MultiIndex if it exists
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # Save CSV
    data.to_csv("../data/sp500.csv")
    print("Data saved to data/sp500.csv")

    return data


if __name__ == "__main__":
    fetch_sp500_data()
