import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
SYMBOLS = ["SPOT", "MSFT", "NVDA"]
BASE_URL = "https://www.alphavantage.co/query"