import yfinance as yf
import pandas as pd
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
from bs4 import BeautifulSoup
import requests
import numpy as np

def get_stock_data(symbol):
    try:
        df = yf.download(symbol, period="3mo", interval="1d", progress=False)
        if df.empty:
            return None
        df["SMA_20"] = df["Close"].rolling(window=20).mean()
        df["EMA_10"] = df["Close"].ewm(span=10, adjust=False).mean()
        return df
    except Exception:
        return None

def predict_price(df):
    try:
        df = df.dropna()
        if len(df) < 2:
            return None
        df["Day"] = range(len(df))
        X = df[["Day"]]
        y = df["Close"]
        model = LinearRegression().fit(X, y)
        next_day = [[len(df)]]
        return model.predict(next_day)[0]
    except:
        return None

def get_sentiment(stock_name):
    try:
        url = f"https://www.moneycontrol.com/news/tags/{stock_name.lower()}.html"
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        headlines = [tag.text for tag in soup.find_all("h2")][:5]
        if not headlines:
            return "No news found"
        text = " ".join(headlines)
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            return "Positive"
        elif polarity < -0.1:
            return "Negative"
        else:
            return "Neutral"
    except:
        return "Sentiment unavailable"
