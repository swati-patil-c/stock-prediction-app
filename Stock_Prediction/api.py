from flask import Flask, request, jsonify
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    stock_name = request.args.get('stock')

    # fetch data
    data = yf.download(stock_name, start="2024-01-02", end="2025-01-02")

    if data.empty:
        return jsonify({"error": "Invalid stock name"}), 400

    # prepare data
    data = data[['Close']].copy()
    data['Prediction'] = data['Close'].shift(-1)
    data.dropna(inplace=True)

    # train model
    X = data[['Close']]
    Y = data['Prediction']

    model = LinearRegression()
    model.fit(X, Y)

    # last price
    Last_price = data['Close'].iloc[-1].item()

    # prediction
    Predicted_price = model.predict(np.array([[Last_price]]))[0]

    # trend
    trend = "UP 📈" if Predicted_price > Last_price else "DOWN 📉"

    # response
    return jsonify({
        "stock": stock_name,
        "last_price": float(Last_price),
        "predicted_price": float(Predicted_price),
        "trend": trend
    })

if __name__ == '__main__':
    app.run(debug=True)