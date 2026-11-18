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

def validate_ticker(ticker):
    try:
        data = yf.download(ticker)
        if data.empty:
            st.error(f'Error fetching data for ticker "{ticker}"! Is the ticker correct?', title='Invalid Ticker')
            return False
        return True
    except Exception as e:
        st.error(f'Error fetching data for ticker "{ticker}": {e}', title='Error')
        return False


st.set_page_config(page_title="Monte Carlo Simulator", page_icon=":chart_with_upwards_trend:", layout="wide")
st.title("Monte Carlo Simulator")
controls = st.container(horizontal_alignment='center', width='stretch', height=100, wrap=False, horizontal=True, vertical_alignment='center')

with controls:
    ticker_input = st.text_input("Enter a stock ticker", value="AAPL", key='ticker', max_chars=14, on_change='ignore')
    iterations_input = st.slider("Number of iterations", min_value=1000, max_value=50000, step=1000, value=10000, on_change='ignore')
    run_button = st.button("Run", type='primary', width=100)
main = st.container()

with main:
    c1, c2 = st.columns([0.8, 0.2])
    c1.subheader(f"Monte Carlo Simulation for {ticker_input}", width='stretch', text_alignment='center')
    chart = c1.line_chart(np.zeros((1,1)), width='stretch')
    with c2:
        st.subheader("Chart Statistics", width='stretch', text_alignment='center')

    if run_button:
        if validate_ticker(ticker_input):
            matrix = monte_carlo(ticker_input, iterations_input)
            tenth_percentile = round(np.percentile(matrix[-1], 10), 2)
            median = round(np.percentile(matrix[-1], 50), 2)
            ninety_percentile = round(np.percentile(matrix[-1], 90), 2)
            ninety_nine_percentile = round(np.percentile(matrix[-1], 99), 2)

            c2.metric(label="10th Percentile", value=tenth_percentile, help=f'Out of {iterations_input} iterations, 90% of the outcomes were above ${tenth_percentile}.')
            c2.metric(label="Median", value=median, help=f'Out of {iterations_input} iterations, 50% of the outcomes were above ${median}.')
            c2.metric(label="90th Percentile", value=ninety_percentile, help=f'Out of {iterations_input} iterations, 10% of the outcomes were above ${ninety_percentile}.')
            c2.metric(label="99th Percentile", value=ninety_nine_percentile, help=f'Out of {iterations_input} iterations, 1% of the outcomes were above ${ninety_nine_percentile}.')
            
            chart.line_chart(matrix, width='stretch')

            
