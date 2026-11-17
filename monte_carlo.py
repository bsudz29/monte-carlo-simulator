import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf


def monte_carlo(ticker, iterations):
    stock_data = yf.download(ticker, period="5y", auto_adjust=False, multi_level_index=False)
    log_returns = np.log(stock_data['Adj Close'] / stock_data['Adj Close'].shift(1)).dropna()
    mu, sigma = log_returns.mean() + 0.5 * log_returns.var(), log_returns.std()
    rng = np.random.default_rng()
    mat = rng.normal(0, 1, (252, iterations))
    mat = np.exp((mu - 0.5 * sigma ** 2) + sigma * mat)
    mat.cumprod(axis=0, out=mat)
    mat = np.vstack([np.ones(mat.shape[1]), mat]) #so that initially all values start at the same value
    mat *= stock_data['Adj Close'].iloc[-1]
    return mat

#ui stuff will go here for plotting, right not call the ticker selected
#from a dropdown into the imported monte-carlo file as a function
st.set_page_config(page_title="Monte Carlo Simulator", page_icon=":chart_with_upwards_trend:", layout="wide")
st.title("Monte Carlo Simulator")
controls = st.container(horizontal_alignment='center', width='stretch', height=100, wrap=False, horizontal=True, vertical_alignment='center')
with controls:
    ticker_input = st.text_input("Enter a stock ticker", value="AAPL", key='ticker', max_chars=14, on_change='ignore')
    iterations_input = st.slider("Number of iterations", min_value=1000, max_value=50000, step=1000, value=10000, on_change='ignore')
    run_button = st.button("Run", type='primary', width=100)
main = st.container()
with main:
    c1, c2 = st.columns([0.5, 0.5])
    c1.subheader(f"Monte Carlo Simulation for {ticker_input}")
    fig, ax = plt.subplots(figsize=(10, 6))
    if run_button:
        ax.plot(monte_carlo(ticker_input, iterations_input))
        c1.pyplot(fig)
