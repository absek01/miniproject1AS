# INF601 - Advanced Programming in Python
# Abhisek Shrestha
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os

# List of stock tickers
tickers = ['AAPL', 'BZFD', 'GOOGL', 'AMZN', 'TSLA']

# Number of trading days
num_days = 5


# Fetching stock data
def fetch_stock_data(tickers, num_days):
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=f'{num_days}d')
        data[ticker] = np.array(hist['Close'])  # Convert to NumPy array
    return data

