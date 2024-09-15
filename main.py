# INF601 - Advanced Programming in Python
# Abhisek Shrestha
# Mini Project 1

#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
#(5/5 points) Proper import of packages used.
#(20/20 points) Using an API of your choice (yfinance works), collect the closing price of 5 of your favorite stock tickers for the last 10 trading days.
#(10/10 points) Store this information in a list that you will convert to a array in NumPy.
#(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring the documentation for matplotlib. At minimum it just needs to show 10 data points.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
import os

# List of stock tickers to fetch data for
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

# Number of trading days to retrieve data for
num_days = 5


def fetch_stock_data(tickers, num_days):

    data = {}
    for ticker in tickers:
        # Fetch historical data for the given ticker symbol
        stock = yf.Ticker(ticker)
        hist = stock.history(period=f'{num_days}d')

        # Convert the 'Close' column to a NumPy array and store in dictionary
        data[ticker] = np.array(hist['Close'])
    return data


def plot_stock_data(data):

    # Create 'charts' directory if it does not exist
    if not os.path.exists('charts'):
        os.makedirs('charts')

    for ticker, prices in data.items():
        # Create a new figure for each ticker
        plt.figure(figsize=(10, 6))

        # Plot closing prices with markers
        plt.plot(prices, marker='o', label=ticker)

        # Set the title and labels
        plt.title(f'Closing Prices for {ticker}')
        plt.xlabel('Days')
        plt.ylabel('Closing Price (USD)')

        # Add grid, legend, and save the plot
        plt.grid(True)
        plt.legend()
        plt.savefig(f'charts/{ticker}_closing_prices.png')
        plt.close()


def main():

    # Fetch stock data
    data = fetch_stock_data(tickers, num_days)

    # Generate and save plots
    plot_stock_data(data)

    # Print a confirmation message
    print("Stock data has been plotted and saved.")


# Entry point of the script
if __name__ == "__main__":
    main()

