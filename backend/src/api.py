from flask import Flask, jsonify
import pandas as pd
from simulate import sma_crossover

app = Flask(__name__)

@app.route("/simulate", methods=["GET"])
def simulate():
    df = pd.read_csv("../data/aapl.csv")
    results = sma_crossover(df)
    return jsonify(results.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
