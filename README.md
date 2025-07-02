# Indian Stock Trend Predictor (NSE/BSE)

A Streamlit web app to predict Indian stock price direction using:
- ✅ Live stock data (NSE & BSE)
- 📰 News headlines
- 🧠 Sentiment analysis
- ⏱️ Auto refresh every 10 mins
- 📉 Visualization & CSV export

## To Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## How Prediction Works

- App pulls current stock data using `yfinance`
- Fetches news articles using `Google News` search
- Analyzes sentiment via `TextBlob`
- Predicts UP 📈 or DOWN 📉 movement accordingly

