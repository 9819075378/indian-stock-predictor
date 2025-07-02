import streamlit as st
import pandas as pd
from utils import get_stock_data, fetch_latest_news, analyze_sentiment
import time

st.set_page_config(page_title="📈 Indian Stock Predictor", layout="wide")
st.title("📊 Indian Stock Trend Predictor (NSE + BSE)")

exchange = st.radio("Choose Exchange", ["NSE", "BSE"])
stock_list = {
    "RELIANCE": "RELIANCE.NS",
    "INFY": "INFY.NS",
    "TCS": "TCS.NS",
    "HDFCBANK": "HDFCBANK.NS",
    "ICICIBANK": "ICICIBANK.NS"
}

if exchange == "BSE":
    stock_list = {k: v.replace(".NS", ".BO") for k, v in stock_list.items()}

stock = st.selectbox("Select a Stock", list(stock_list.keys()))
symbol = stock_list[stock]

data_load_state = st.text("Fetching stock data...")
data = get_stock_data(symbol)
data_load_state.text("")

st.subheader("Raw data preview:")
st.dataframe(data.tail(10))

st.subheader("Sentiment Analysis (Last 5 News Headlines)")
news = fetch_latest_news(stock)
sentiment = analyze_sentiment(news)
st.write(f"📰 News Sentiment: **{sentiment}**")
st.write("Recent Headlines:")
for n in news:
    st.markdown(f"- {n}")

st.subheader("📈 Stock Close Price with SMA and EMA")
st.line_chart(data[['Close', 'SMA_20', 'EMA_10']])

st.caption("⏱️ Auto-refreshes every 10 minutes.")
time.sleep(600)
