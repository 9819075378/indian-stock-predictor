import yfinance as yf
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

def get_stock_data(symbol):
    data = yf.download(tickers=symbol, period='1d', interval='5m')
    return data

def fetch_latest_news(company):
    query = company + " stock news"
    url = f"https://news.google.com/search?q={query}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    headlines = soup.select("article h3")
    return [h.get_text() for h in headlines[:5]]

def analyze_sentiment(news_list):
    all_text = " ".join(news_list)
    sentiment = TextBlob(all_text).sentiment.polarity
    return "Positive" if sentiment > 0 else "Negative"
