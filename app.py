import streamlit as st
import pandas as pd
from utils import get_stock_data, fetch_latest_news, analyze_sentiment
import time

st.set_page_config(page_title="Indian Stock Predictor", layout="wide")

st.title("Indian Stock Trend Predictor (NSE)")

stock_list = {
    "RELIANCE": "RELIANCE.NS",
    "INFY": "INFY.NS",
    "TCS": "TCS.NS",
    "HDFCBANK": "HDFCBANK.NS",
    "ICICIBANK": "ICICIBANK.NS"
}

stock = st.selectbox("Select a Stock", list(stock_list.keys()))
symbol = stock_list[stock]

with st.spinner("Fetching latest stock data..."):
    data = get_stock_data(symbol)

if data is None or data.empty:
    st.error("Unable to fetch stock data. Please try again later.")
else:
    st.subheader("Latest Stock Data")
    st.line_chart(data['Close'])

    st.subheader("Latest News Headlines")
    news = fetch_latest_news()
    if not news:
        st.warning("No news available at the moment.")
    else:
        for item in news:
            st.write("- " + item)

        st.subheader("News Sentiment")
        sentiment = analyze_sentiment(news)
        st.write(sentiment)

        st.subheader("Predicted Direction")
        if sentiment == "Positive":
            st.success("UP")
        else:
            st.error("DOWN")

st.caption("Auto-refresh every 10 minutes enabled.")
time.sleep(600)
st.experimental_rerun()
