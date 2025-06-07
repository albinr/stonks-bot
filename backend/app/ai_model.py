# backend/app/ai_model.py

import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
from pathlib import Path

MODEL_DIR = Path("models")
MODEL_DIR.mkdir(exist_ok=True)
MODEL_PATH = MODEL_DIR / "model.pkl"


def create_model() -> LinearRegression:
    return LinearRegression()

def train_model(model: LinearRegression, X: np.ndarray, y: np.ndarray) -> LinearRegression:
    model.fit(X, y)
    return model

def save_model(model: LinearRegression) -> None:
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

def load_model() -> LinearRegression:
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

def predict(model: LinearRegression, X: np.ndarray) -> np.ndarray:
    return model.predict(X)
