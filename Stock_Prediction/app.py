import yfinance as yf

# take input from user
stock_name = input("Enter stock name (e.g. AAPL, TSLA): ")

# fetch data
data = yf.download(stock_name, start="2023-01-01", end="2024-01-01")

print(data.head())