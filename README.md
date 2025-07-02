# Indian Stock Predictor App (NSE + BSE)

A Streamlit app that:
- Predicts stock price trends using SMA & EMA
- Performs sentiment analysis on latest news
- Supports NSE & BSE stock exchanges
- Auto-refreshes every 10 minutes

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Features
- News scraped from Moneycontrol and Economic Times
- 5-minute interval data via yfinance
- Plots with moving averages (SMA 20, EMA 10)

Enjoy trading smarter!
