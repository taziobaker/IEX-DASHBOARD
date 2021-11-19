import streamlit as st
import requests
import config

from helpers import format_number

symbol = st.sidebar.text_input("Symbol", value="AMC")

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership', 'Technicals'))

st.title(screen)

if screen == 'Overview':
  url = f"https://cloud.iexapis.com/stable/tops?token={config.sk_05f62d0b97b84cfbb15650bc980058b0}&symbols={symbol}%lastSalePrice"
  r = requests.get(url)
  response_Fjson = r.json()

  url = f"https://cloud.iexapis.com/stable/stock/{symbol}/quote/iexRealtimePrice?token={config.sk_05f62d0b97b84cfbb15650bc980058b0}"
  r = requests.get(url)
  response_Qjson = r.json()
  
  col1, col2 = st.columns (2)
  
  with col1:
    #st.subheader.write("FREE:")
    st.write(response_Fjson)
  
  with col2:
    #st.subheader.write("QUOTE:")
    st.write(response_Qjson)
  
  

if screen == 'Fundamentals':
  pass

# Free IEX price for AMC
#https://cloud.iexapis.com/stable/tops?token=YOUR_TOKEN_HERE&symbols=amc
#Stock quote for AMC
#https://cloud.iexapis.com/stable/stock/amc/quote?token=YOUR_TOKEN_HERE
