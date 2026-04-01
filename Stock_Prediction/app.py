import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#take input
stock_name = input("Enter the stock name : ")
#fetch the data 
data = yf.download(stock_name, start="2024-01-02", end="2025-01-02")

if data.empty:
    print("Invalid data stock!")
    exit()

#select  important colume
print("latest data of stock :" , data.tail())
#use close price only
data = data[['Close']].copy()

#create a prediction column
data['Prediction'] = data['Close'].shift(-1)

#remove the last row
data = data.dropna()
#define x and y
X = data[['Close']]
Y = data['Prediction']

model = LinearRegression()
model.fit(X, Y)

Last_price = data['Close'].iloc[-1].item()
Predicted_price = model.predict(np.array([[Last_price]]))[0]

#result
print("Result")
print("Last closing price :" , Last_price)
print("predicted price : ", Predicted_price)

#trend
if Predicted_price > Last_price:
    print("Trend is up!!")
else:
    print("Trend is down!!")

