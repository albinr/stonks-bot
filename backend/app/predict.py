# backend/app/predict.py

from app import ai_model
import numpy as np

def main():
    model = ai_model.load_model()

    # Example: Predict using a made-up feature vector
    # Replace this with real input matching your training data structure
    example_input = np.array([[130.5]])  # shape (1, n_features)

    prediction = ai_model.predict(model, example_input)
    print(f"📈 Prediction for input {example_input[0][0]}: {prediction[0]}")

if __name__ == "__main__":
    main()
