import streamlit as st
import requests
import json
import sys
import pandas as pd
import altair as alt

st.set_page_config(page_title="Alerts Stock")

st.title("Alerts Stock")

st.sidebar.image("https://miro.medium.com/max/1000/1*B_R11J_9G4U3lac0omktLQ.png", width=100,
                 channels='BGR', output_format='PNG')

# st.sidebar.header("Alerts Stock")
# with st.sidebar.expander("Info"):
#     st.info(f"""
#         Click [here](https://finance.yahoo.com/cryptocurrencies/)
#         for a list of cryptocurrencies symbols on Yahoo Finance.
#         """)

name_of_stock = st.sidebar.text_input("Enter name of the stock")
trend = st.sidebar.selectbox(
    'Select the Trend',
    ('Up Trend', 'Down Trend'))
price_trigger = st.sidebar.text_input("Enter the price trigger")

if st.sidebar.button('Submit'):
    st.sidebar.write('Why hello there')
else:
    st.sidebar.write('')


