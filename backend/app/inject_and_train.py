# backend/app/inject_and_train.py

import random
import time
from app import fetch_data, ai_model
import numpy as np
import pandas as pd

# List of tickers to randomly inject from
TICKERS = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"]

# Number of injections to simulate
NUM_INJECTIONS = 10

# Tracking scores
correct_predictions = 0

for i in range(NUM_INJECTIONS):
    print(f"\n🔁 Injection {i+1}/{NUM_INJECTIONS}")

    # 1. Choose random ticker
    symbol = random.choice(TICKERS)
    print(f"📊 Chosen symbol: {symbol}")

    # 2. Fetch data
    df = fetch_data.fetch_daily(symbol, outputsize="compact")
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df = df.dropna(subset=["Close"])

    if df is None or len(df) < 2:
        print("⚠️ Not enough data, skipping")
        continue

    # 3. Choose a random time index that allows a t+1 comparison
    index = random.randint(0, len(df) - 2)
    X = np.array([[df.iloc[index]["Close"]]])
    actual_next_close = df.iloc[index + 1]["Close"]

    # 4. Load or create model
    try:
        model = ai_model.load_model()
    except FileNotFoundError:
        model = ai_model.create_model()

    # 5. Predict next day's close
    predicted = ai_model.predict(model, X)[0]
    print(f"   🔮 Predicted: {predicted:.2f}, Actual: {actual_next_close:.2f}")

    # 6. Reward if close enough
    if abs(predicted - actual_next_close) / actual_next_close < 0.05:
        correct_predictions += 1
        print("   ✅ Good prediction (+1)")
    else:
        print("   ❌ Bad prediction")

    # 7. Train on this data point (supervised learning simulation)
    model = ai_model.train_model(model, X, np.array([actual_next_close]))
    ai_model.save_model(model)

    time.sleep(1)  # to avoid API rate limits

print(f"\n🏁 Injections complete. Score: {correct_predictions}/{NUM_INJECTIONS} good predictions.")
