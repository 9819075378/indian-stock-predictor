# 📈 Indian Stock Trend Predictor (NSE)

This is a Streamlit web app that predicts **Indian stock market trends** (UP or DOWN) for selected NSE stocks using:

- 📉 Real-time stock data (via `yfinance`)
- 📰 Latest market news headlines
- 🤖 Sentiment analysis (via TextBlob)

---

## 🚀 Features

✅ Select from popular NSE stocks (e.g., RELIANCE, TCS, INFY)  
✅ Auto-refreshes every 10 minutes  
✅ Live price chart  
✅ Top 5 news headlines scraped from Economic Times  
✅ Sentiment-based UP/DOWN prediction  

---

## 🛠️ How to Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/indian-stock-predictor.git
cd indian-stock-predictor

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

---

## 📦 Requirements

- Python 3.7+
- Streamlit
- yfinance
- textblob
- beautifulsoup4
- pandas
- requests
- lxml

---

## 🌐 Deployed App

👉 [Live App Link](https://your-streamlit-url)

---

## 🙌 Contributions

Pull requests welcome! Feel free to suggest new features like:
- ML models for better prediction
- More visualizations
- News from multiple sources

---
