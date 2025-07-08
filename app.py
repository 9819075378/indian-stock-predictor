import streamlit as st
from utils import get_stock_data, predict_price, get_sentiment

st.set_page_config(page_title="Indian Stock Predictor", layout="wide")
st.title("📈 Indian Stock Predictor (NSE)")

symbol = st.selectbox("Select NSE Stock Symbol", get_stock_data().columns.levels[1].tolist())

if st.button("Analyze"):
    df, fig = get_stock_data(symbol)
    st.plotly_chart(fig, use_container_width=True)
    pred = predict_price(df)
    sentiment = get_sentiment()
    st.subheader(f"📊 Predicted Close Price (Next Day): ₹{pred:.2f}")
    st.markdown(f"🗞️ **Market Sentiment:** {sentiment}")
