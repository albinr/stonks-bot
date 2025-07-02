import sqlite3
from datetime import date, timedelta

def show_daily_summary(db_path="stocks.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    today = date.today()
    yesterday = today - timedelta(days=1)

    # Konvertera till stringformat (ex: 2025-07-02)
    today_str = today.isoformat()
    yest_str = yesterday.isoformat()

    cursor.execute("""
        SELECT s1.symbol, s1.close, s2.close
        FROM stock_prices s1
        JOIN stock_prices s2 ON s1.symbol = s2.symbol
        WHERE s1.date = ? AND s2.date = ?
    """, (today_str, yest_str))

    rows = cursor.fetchall()

    print(f"\n📊 Dagens aktieöversikt ({today_str})\n")
    for symbol, close_today, close_yest in rows:
        change = close_today - close_yest
        percent = (change / close_yest) * 100

        if change > 0:
            arrow = "📈"
            color = "\033[92m"  # Grön
        elif change < 0:
            arrow = "📉"
            color = "\033[91m"  # Röd
        else:
            arrow = "→"
            color = "\033[0m"   # Neutral

        print(f"{color}{symbol}: {arrow} {close_yest:.2f} → {close_today:.2f} ({percent:+.2f}%)\033[0m")

    conn.close()
