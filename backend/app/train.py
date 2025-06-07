# backend/app/train.py

import pandas as pd
from app import fetch_data, ai_model
MODEL_PATH = "model.pkl"

def main():
    symbol = "AAPL"
    df = fetch_data.fetch_daily(symbol)

    # Drop rows with missing data
    df = df.dropna()

    # Feature: Previous day's closing price
    df["PrevClose"] = df["Close"].shift(1)
    df = df.dropna()

    # Target: Today's closing price
    X = df[["PrevClose"]].values
    y = df["Close"].values

    model = ai_model.create_model()
    trained_model = ai_model.train_model(model, X, y)
    ai_model.save_model(trained_model)

    print("✅ Model trained and saved.")

if __name__ == "__main__":
    main()
