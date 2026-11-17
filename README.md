# Monte Carlo Stock Simulator

A Python web app built with Streamlit that visualizes possible stock price paths over one trading year. It uses five years of historical adjusted closing prices from Yahoo Finance to estimate daily log returns and volatility, then generates randomized price paths starting from the latest adjusted closing price.

## Features

- Enter a stock ticker, such as `AAPL`.
- Generate 1,000–50,000 simulated paths across 252 trading days.
- View the paths in a Matplotlib chart within the app.

## Getting started

You can view the project and test out the different features here:
[Try the live demo](https://monte-carlo-simulator-farduj7wkzrkrahipueyih.streamlit.app/)

If you'd like to run it on your own machine:
With Python installed, run these commands from the project directory:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run monte_carlo.py
```

On Windows, activate the environment with `.venv\Scripts\activate` instead.

Open the local URL displayed by Streamlit, enter a ticker, choose the number of iterations, and click **Run**. An internet connection is required to download historical prices.

## How it works

The simulator models daily price changes using normally distributed logarithmic returns estimated from historical data obtained from Yahoo Finance. Each run produces a new set of random paths; more iterations provide more scenarios and take longer to plot.

The model assumes historical return patterns and volatility remain constant. The results illustrate possible outcomes but lack information regarding breaking news, market shocks, or other changing conditions. 
