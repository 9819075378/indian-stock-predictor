import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
from sklearn.linear_model import LinearRegression
import numpy as np

def get_stock_data(symbol="RELIANCE.NS"):
    df = yf.download(symbol, period="6mo", interval="1d")
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['EMA_10'] = df['Close'].ewm(span=10, adjust=False).mean()
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name="Close"))
    fig.add_trace(go.Scatter(x=df.index, y=df['SMA_20'], name="SMA 20"))
    fig.add_trace(go.Scatter(x=df.index, y=df['EMA_10'], name="EMA 10"))
    return df, fig

def predict_price(df):
    df = df.dropna()
    X = np.arange(len(df)).reshape(-1,1)
    y = df['Close'].values
    model = LinearRegression()
    model.fit(X, y)
    return model.predict([[len(df)+1]])[0]

def get_sentiment():
    try:
        url = "https://www.moneycontrol.com/news/business/markets/"
        page = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(page.content, "html.parser")
        headlines = [a.text for a in soup.select("h2")[:5]]
        blob = TextBlob(" ".join(headlines))
        polarity = blob.sentiment.polarity
        if polarity > 0.1:
            return "Positive"
        elif polarity < -0.1:
            return "Negative"
        else:
            return "Neutral"
    except:
        return "Unavailable"
