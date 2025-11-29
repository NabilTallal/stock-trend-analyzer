# 📈 Stock Market Trend Analyzer

**Analyze S&P 500 historical trends with interactive visualizations using Python.**

This project fetches historical stock data, calculates key metrics like **daily returns**, **moving averages**, and **volatility**, and provides **interactive charts** for exploring trends. Perfect for a data analytics portfolio or learning stock market analysis.

---

## Features
- Fetch historical S&P 500 data automatically using `yfinance`.
- Clean and explore stock data with Pandas.
- Calculate **daily returns**, **rolling moving averages**, and **volatility**.
- Visualize trends using:
  - **Matplotlib** (static plots)
  - **Plotly** (interactive charts)
  - **Streamlit dashboard** (interactive web app)
- Filter data by **date range** and adjust **moving average windows**.
- Optional display of raw data and daily returns.

---

## Tech Stack
- Python 3.10+
- Pandas
- Matplotlib
- Plotly
- Streamlit
- yfinance

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/stock-trend-analyzer.git
cd stock-trend-analyzer
```

2. **Create a virtual environment**
```bash
python -m venv .venv

# Windows
source .venv/Scripts/activate

# Mac/Linux
source .venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## Usage

1. **Fetch the latest S&P 500 data**
```bash
python src/fetch_data.py
```

2. **Explore the data**
```bash
python src/explore_data.py
```

3. **Analyze trends**
```bash
python src/analysis.py
```

4. **Interactive Plotly chart**
```bash
python src/dashboard_plotly.py
```

5. **Streamlit Dashboard**
```bash
streamlit run src/dashboard_streamlit.py
```

---

## Dashboard Features
- **Select date range**
- **Adjust moving average window**
- **Toggle daily returns**
- **View raw data**

---

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
