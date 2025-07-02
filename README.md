# 📈 Indian Stock Predictor App (NSE + BSE)

A powerful Streamlit web app to help you:

- 🔍 Predict stock price trends using **moving averages** (SMA & EMA)
- 🧠 Analyze latest market **news sentiment**
- 📉 Forecast the **next day’s closing price** using **machine learning (Linear Regression)**
- ✅ Supports both **NSE** and **BSE** stock exchanges

---

## 💡 Features

✅ Choose stocks from NSE or BSE  
✅ Auto-refresh every 10 minutes  
✅ Scrapes live news headlines from Moneycontrol & Economic Times  
✅ Clean visualization of stock price trends  
✅ Predicted price for tomorrow using Linear Regression

---

## 📦 Setup Instructions (Local)

```bash
git clone https://github.com/yourusername/indian-stock-predictor.git
cd indian-stock-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## 🗃️ Files Required

- `app.py` → Main Streamlit app  
- `utils.py` → Data fetching, sentiment & prediction logic  
- `requirements.txt` → All Python dependencies  
- `nse_stocks.csv` → List of NSE companies  
- `bse_stocks.csv` → List of BSE companies  

---

## 🚀 Live Demo (Optional)

If deployed via Streamlit Cloud, paste your live link here:

👉 [https://share.streamlit.io/yourusername/indian-stock-predictor](https://share.streamlit.io/yourusername/indian-stock-predictor)

---

## 👨‍💻 Built With

- [Streamlit](https://streamlit.io)  
- [yFinance](https://pypi.org/project/yfinance/)  
- [scikit-learn](https://scikit-learn.org)  
- [TextBlob](https://textblob.readthedocs.io/)  
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)