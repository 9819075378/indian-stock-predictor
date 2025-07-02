import yfinance as yf
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

def get_stock_data(symbol):
    try:
        data = yf.download(tickers=symbol, period='1d', interval='5m')
        return data
    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None

def fetch_latest_news():
    try:
        url = "https://economictimes.indiatimes.com/markets"
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "lxml")
        headlines = [item.text.strip() for item in soup.select(".eachStory h3")[:5]]
        return headlines
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []

def analyze_sentiment(news_list):
    polarity = 0
    for news in news_list:
        blob = TextBlob(news)
        polarity += blob.sentiment.polarity
    return "Positive" if polarity > 0 else "Negative"