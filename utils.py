import yfinance as yf
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_stock_data(symbol):
    data = yf.download(tickers=symbol, period='1d', interval='5m')
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['EMA_10'] = data['Close'].ewm(span=10, adjust=False).mean()
    return data

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
    news_mc = fetch_moneycontrol_news(company)
    news_et = fetch_economic_times_news(company)
    return news_mc + news_et

def analyze_sentiment(news_list):
    all_text = " ".join(news_list)
    sentiment = TextBlob(all_text).sentiment.polarity
    return "Positive" if sentiment > 0 else "Negative"
