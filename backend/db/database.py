import sqlite3

conn = sqlite3.connect("stocks.db", check_same_thread=False)
cursor = conn.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            date TEXT NOT NULL,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume INTEGER,
            UNIQUE(symbol, date)
        )
    """)
    conn.commit()
