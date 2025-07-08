import streamlit as st
import pandas as pd
from utils import get_stock_data, predict_price, get_sentiment

st.set_page_config(page_title="Indian Stock Predictor", layout="wide")
st.title("📈 Indian Stock Predictor (NSE)")

# Load NSE symbols from CSV
symbols_df = pd.read_csv("nse_stocks.csv")
symbols = symbols_df["Symbol"].dropna().unique().tolist()
selected_symbol = st.selectbox("Select NSE Stock Symbol", symbols)

if st.button("Analyze"):
    full_symbol = selected_symbol + ".NS"
    df, fig = get_stock_data(full_symbol)
    st.plotly_chart(fig, use_container_width=True)

    if df is not None and not df.empty:
        pred = predict_price(df)
        sentiment = get_sentiment()
        # Ensure pred is a scalar for formatting
        try:
            pred_value = float(pred[0])
        except (TypeError, IndexError):
            pred_value = float(pred)
        st.subheader(f"📊 Predicted Close Price (Next Day): ₹{pred_value:.2f}")
        st.markdown(f"🗞️ **Market Sentiment:** {sentiment}")
    else:
        st.error("Failed to retrieve data. Please check the symbol or try again later.")
