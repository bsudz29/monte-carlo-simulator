import streamlit as st
import matplotlib.pyplot as plt
import monte_carlo


def run(ticker, iterations):
    pass

#ui stuff will go here for plotting, right not call the ticker selected
#from a dropdown into the imported monte-carlo file as a function
st.title("Monte Carlo Interactive Simulator")
controls = st.container(horizontal_alignment='center', width='stretch', height=100)
with controls:
    ticker_input = st.text_input("Enter a stock ticker", value="AAPL", key='ticker', max_chars=14)
    iterations_input = st.slider("Number of iterations", min_value=1000, max_value=50000, step=1000, value=10000)
    run_button = st.button("Run")