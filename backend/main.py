from apscheduler.schedulers.blocking import BlockingScheduler
from services.alpha import fetch_and_save_stock_data
from dashboard.daily_summary import show_daily_summary

scheduler = BlockingScheduler()

# Kör varje dag kl 18:00
@scheduler.scheduled_job('cron', hour=18, minute=0)
def scheduled_job():
    print("Hämtar dagsdata...")
    fetch_and_save_stock_data()

# if __name__ == "__main__":
#     print("Stonks bot startad. Väntar på nästa körning...")
#     scheduler.start()

if __name__ == "__main__":
    print("🔁 Hämtar aktiedata...")
    fetch_and_save_stock_data()
    print("✅ Data sparad!")

    show_daily_summary()