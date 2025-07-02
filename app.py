import streamlit as st
import pandas as pd
from utils import get_stock_data, fetch_latest_news, analyze_sentiment
import time

st.set_page_config(page_title="📊 Indian Stock Predictor", layout="wide", page_icon="📈")
st.title("📊 Indian Stock Trend Predictor (NSE/BSE)")

# Stock list with NSE and BSE codes
stock_list = {
    "RELIANCE (NSE)": "RELIANCE.NS",
    "RELIANCE (BSE)": "500325.BO",
    "TCS (NSE)": "TCS.NS",
    "TCS (BSE)": "532540.BO",
    "INFY (NSE)": "INFY.NS",
    "INFY (BSE)": "500209.BO",
    "HDFCBANK (NSE)": "HDFCBANK.NS",
    "HDFCBANK (BSE)": "500180.BO",
    "ICICIBANK (NSE)": "ICICIBANK.NS",
    "ICICIBANK (BSE)": "532174.BO"
}

stock = st.selectbox("Select a Stock", list(stock_list.keys()))
symbol = stock_list[stock]

# Auto-refresh every 10 minutes
st_autorefresh = st.experimental_rerun
refresh_interval = 600  # seconds

# Get stock data
df = get_stock_data(symbol)
st.subheader("📉 Raw data preview:")
st.dataframe(df.tail(10))

# Chart
st.line_chart(df['Close'])

# News & Sentiment
st.subheader("📰 Latest News & Sentiment")
news = fetch_latest_news(stock.split()[0])
for n in news:
    st.markdown(f"- {n}")

sentiment = analyze_sentiment(news)
st.markdown(f"**🧠 Sentiment Analysis**: `{sentiment}`")

# Simple prediction based on sentiment
prediction = "📈 Price likely to go UP" if sentiment == "Positive" else "📉 Price likely to go DOWN"
st.subheader("🔮 Prediction:")
st.markdown(f"### {prediction}")

# Download button
st.download_button("Download CSV", df.to_csv().encode('utf-8'), "stock_data.csv", "text/csv")
