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

# Creating and saving plots
def plot_stock_data(data):
    if not os.path.exists('charts'):
        os.makedirs('charts')

    for ticker, prices in data.items():
        plt.figure(figsize=(10, 6))
        plt.plot(prices, marker='o', label=ticker)
        plt.title(f'Closing Prices for {ticker}')
        plt.xlabel('Days')
        plt.ylabel('Closing Price (USD)')
        plt.grid(True)
        plt.legend()
        plt.savefig(f'charts/{ticker}_closing_prices.png')
        plt.close()
