"""
Needed:
- Numpy
- MatPlotLib
- Streamlit
- Random
- about 1-5 years of past stock data
    - 
- iterations roughly 1k - 50k

"""
import numpy as np
import yfinance as yf
import pandas as pd
import random

ticker = yf.Ticker('AAPL')
df = pd.DataFrame(ticker.history(period='5y'))
df = df[::-1] #originally sorted oldest - newest
print(df)