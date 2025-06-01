import requests
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
URL = "https://www.alphavantage.co/query"

def fetch_daily(symbol: str, outputsize: str = "compact") -> pd.DataFrame:
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY,
        "outputsize": outputsize,
        "datatype": "json"
    }
    print(f"Fetching {symbol} ({outputsize})...")
    response = requests.get(URL, params=params)
    data = response.json()

    if "Time Series (Daily)" not in data:
        raise Exception(f"Alpha Vantage Error: {data.get('Note') or data.get('Error Message') or data}")
    df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient="index")
    df = df.rename(columns = {
        "1. open": "Open",
        "2. high": "High",
        "3. low": "Low",
        "4. close": "Close",
        "5. volume": "Volume"
    })
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    return df

def save_csv(df: pd.DataFrame, symbol: str):
    os.makedirs("data", exist_ok=True)
    now = datetime.now().strftime("%Y%m%d_%H%M")
    path = f"data/{symbol.upper()}_{now}.csv"
    df.to_csv(path, index_label="Date")
    print(f"Saved: {path}")

if __name__ == "__main__":
    symbol = input("Enter stock symbol (e.g. AAPL): ").strip().upper()
    outputsize = input("Output size (compact/full): ").strip() or "compact"

    try:
        df = fetch_daily(symbol, outputsize)
        save_csv(df, symbol)
    except Exception as e:
        print(f"Error: {e}")