import streamlit as st
from utils import get_stock_data, predict_price, get_sentiment
import pandas as pd

st.set_page_config(page_title="Indian Stock Predictor (NSE Only)", layout="wide")

st.title("📈 Indian Stock Predictor (NSE Only)")

# Load stock list
nse_stocks = pd.read_csv("nse_stocks.csv")
stock_options = nse_stocks["Symbol"].dropna().sort_values().tolist()

selected_symbol = st.selectbox("Select NSE Stock", stock_options)
full_symbol = f"{selected_symbol}.NS"

if st.button("🔍 Analyze"):
    with st.spinner("Fetching data and generating prediction..."):
        df = get_stock_data(full_symbol)

        if df is None or df.empty or "Close" not in df.columns:
            st.error("❌ Could not retrieve stock data. Please try a different symbol.")
        else:
            st.success("✅ Data fetched successfully!")

            if all(col in df.columns for col in ["Close", "SMA_20", "EMA_10"]):
                st.subheader("📊 Price Trend with SMA/EMA")
                st.line_chart(df[["Close", "SMA_20", "EMA_10"]])
            else:
                st.warning("⚠️ Not enough data to plot SMA/EMA.")

            st.subheader("🧠 News Sentiment")
            sentiment = get_sentiment(selected_symbol)
            st.write(f"Sentiment: **{sentiment}**")

            st.subheader("📉 Tomorrow's Price Prediction")
            predicted_price = predict_price(df)
            if predicted_price:
                st.metric(label="Predicted Closing Price", value=f"₹{predicted_price:.2f}")
            else:
                st.error("⚠️ Unable to generate prediction due to insufficient data.")
