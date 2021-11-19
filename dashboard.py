import streamlit as st
import requests
import config

symbol = st.sidebar.text_input("Symbol", value="AMC")

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership', 'Technicals'))

st.title(screen)

if screen == 'Overview':
  url = f"https://cloud.iexapis.com/stable/stock/amc/logo?token={config.IEX_API_TOKEN}"
  r = requests.get(url)
  response_json = r.json()
  st.image(response_json['url'])
  
  
    
    #/stock/{symbol}/logo

if screen == 'Fundamentals':
  pass

# Free IEX price for AMC
#https://cloud.iexapis.com/stable/tops?token=YOUR_TOKEN_HERE&symbols=amc
#Stock quote for AMC
#https://cloud.iexapis.com/stable/stock/amc/quote?token=YOUR_TOKEN_HERE
