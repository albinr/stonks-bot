import requests
from config import API_KEY, SYMBOLS, BASE_URL
from db.database import conn, cursor, create_table

def fetch_and_save_stock_data():
    create_table()

    for symbol in SYMBOLS:
        print(f"Hämtar data för {symbol}...")

        params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "apikey": API_KEY
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        try:
            time_series = data["Time Series (Daily)"]
            latest_date = sorted(time_series.keys(), reverse=True)[0]
            daily_data = time_series[latest_date]

            cursor.execute("""
                INSERT OR IGNORE INTO stock_prices 
                (symbol, date, open, high, low, close, volume)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                symbol,
                latest_date,
                float(daily_data["1. open"]),
                float(daily_data["2. high"]),
                float(daily_data["3. low"]),
                float(daily_data["4. close"]),
                int(daily_data["5. volume"])
            ))

            conn.commit()
            print(f"{symbol} för {latest_date} sparad.")

        except KeyError:
            print(f"Något gick fel för {symbol}: {data}")

