import yfinance as yf
import pandas as pd
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import requests
from bs4 import BeautifulSoup

def get_stock_data(symbol):
    try:
        df = yf.download(tickers=symbol, period='10d', interval='1d')
        df['SMA_20'] = df['Close'].rolling(window=3).mean()
        df['EMA_10'] = df['Close'].ewm(span=3, adjust=False).mean()
        return df
    except:
        return pd.DataFrame()

def predict_price(df):
    df = df.dropna()
    if len(df) < 5: return 0.0
    df = df.reset_index()
    df['Day'] = range(len(df))
    X = df[['Day']]
    y = df['Close']
    model = LinearRegression().fit(X, y)
    return model.predict([[len(df)]])[0]

def fetch_moneycontrol_news(company):
    query = company.replace(" ", "-").lower()
    url = f"https://www.moneycontrol.com/news/tags/{query}.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    headlines = soup.select("li.clearfix a")
    return [a.get_text().strip() for a in headlines[:5]]

def fetch_economic_times_news(company):
    url = f"https://economictimes.indiatimes.com/topic/{company.replace(' ', '-')}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    headlines = soup.select("ul.topicstry li h3")
    return [h.get_text().strip() for h in headlines[:5]]

def fetch_latest_news(company):
    try:
        return fetch_moneycontrol_news(company) + fetch_economic_times_news(company)
    except:
        return []

def analyze_sentiment(news_list):
    text = " ".join(news_list)
    score = TextBlob(text).sentiment.polarity
    return "Positive" if score > 0 else "Negative"
