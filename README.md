# 📈 Indian Stock Predictor App (NSE)

A powerful Streamlit web app to help you:

- 🔍 Predict stock price trends using **moving averages** (SMA & EMA)
- 🧠 Analyze latest market **news sentiment**
- 📉 Forecast the **next day’s closing price** using **machine learning (Linear Regression)**
- ✅ Supports **all NSE-listed stocks**

---

## 💡 Features

✅ Choose from full NSE stock list  
✅ Auto-refresh every 10 minutes  
✅ Live news sentiment from Moneycontrol  
✅ Clean price trend visualization (Plotly)  
✅ Tomorrow’s price forecast using Linear Regression

---

## 📦 Setup Instructions (Local)

To run the app locally:

```bash
git clone https://github.com/yourusername/indian-stock-predictor.git
cd indian-stock-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## 🗃️ Files Included

- `app.py` → Main Streamlit app  
- `utils.py` → Data fetching, sentiment & prediction logic  
- `requirements.txt` → All dependencies  
- `nse_stocks.csv` → Full list of NSE companies  

---

## 🚀 Live Demo (Optional)

If deployed via Streamlit Cloud:

👉 https://share.streamlit.io/yourusername/indian-stock-predictor

---

## 👨‍💻 Built With

- Streamlit  
- yFinance  
- Scikit-learn  
- TextBlob  
- BeautifulSoup4  
