import streamlit as st
import requests
import config

from helpers import format_number

symbol = st.sidebar.text_input("Symbol", value="AMC")

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership', 'Technicals'))

st.title(screen)

if screen == 'Overview':
  FREE = f"https://cloud.iexapis.com/stable/tops?token={config.IEX_API_TOKEN}&symbols={symbol}"
  r = requests.get(FREE)
  response_json = r.json()
  st.write
  QUOTE = f"https://cloud.iexapis.com/stable/stock/{symbol}/quote?token={config.IEX_API_TOKEN}"
  r = requests.get(QUOTE)
  response_json = r.json()
  
  col1, col2 = st.beta_columns (2)
  
  with col1:
    st.subheader.write("FREE:")
    st.write(FREE)
  
  with col2:
    st.subheader.write("QUOTE:")
    st.write(QUOTE)
  
  

if screen == 'Fundamentals':
  pass

# Free IEX price for AMC
#https://cloud.iexapis.com/stable/tops?token=YOUR_TOKEN_HERE&symbols=amc
#Stock quote for AMC
#https://cloud.iexapis.com/stable/stock/amc/quote?token=YOUR_TOKEN_HERE
