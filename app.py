import streamlit as st
import pandas as pd
from utils import get_stock_data, fetch_latest_news, analyze_sentiment, predict_price

st.set_page_config(page_title="📈 Indian Stock Predictor", layout="wide")
st.title("📊 Indian Stock Trend Predictor (NSE + BSE)")

# Load stock lists
nse_df = pd.read_csv("nse_stocks.csv")
bse_df = pd.read_csv("bse_stocks.csv")

exchange = st.radio("Choose Exchange", ["NSE", "BSE"])
if exchange == "NSE":
    options = {f"{row['SYMBOL']} - {row['NAME OF COMPANY']}": row['SYMBOL'] + ".NS" for _, row in nse_df.iterrows()}
else:
    options = {f"{row['Scrip Id']} - {row['Scrip Name']}": str(row['Scrip Id']) + ".BO" for _, row in bse_df.iterrows()}

stock_display = st.selectbox("Select a Stock", list(options.keys()))
symbol = options[stock_display]

st.info(f"Fetching data for: `{symbol}`")
data = get_stock_data(symbol)
if data.empty:
    st.error("No stock data found.")
    st.stop()

st.subheader("📉 Recent Prices")
st.dataframe(data.tail(10))

st.subheader("📈 Chart (Close + SMA + EMA)")
plot_cols = [col for col in ['Close', 'SMA_20', 'EMA_10'] if col in data.columns]
if plot_cols:
    st.line_chart(data[plot_cols])

st.subheader("🔮 Predicted Price for Tomorrow")
prediction = predict_price(data)
st.success(f"Predicted Closing Price: ₹{prediction:.2f}")

st.subheader("📰 News & Sentiment")
news = fetch_latest_news(stock_display.split('-')[0].strip())
sentiment = analyze_sentiment(news)
st.markdown(f"**Sentiment**: `{sentiment}`")
for line in news:
    st.markdown(f"- {line}")

st.caption("⏱️ App refreshes every 10 minutes.")
