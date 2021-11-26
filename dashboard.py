import streamlit as st
import requests
import config

from helpers import format_number

symbol = st.sidebar.text_input("Symbol", value="AMC")

screen = st.sidebar.selectbox("View", ('Overview', 'Fundamentals', 'News', 'Ownership', 'Technicals'))

st.title(screen)

if screen == 'Overview':
  #url = f"https://cloud.iexapis.com/stable/tops?token={st.secrets["db_token"]}&symbols={symbol}"
  #r = requests.get(url)
  #response_Fjson = r.json()

  url = f"https://cloud.iexapis.com/stable/stock/{symbol}/quote/iexRealtimePrice?token={st.secrets["db_token"]}"
  r = requests.get(url)
  response_Qjson = r.json()
  
  #url = f"https://cloud.iexapis.com/stable/stock/{symbol}/chart/1d?token={st.secrets["db_token"]}"
  #r = requests.get(url)
  #response_Cjson = r.json()
  
  #col1, col2 = st.columns (2)
  
  #with col1:
    #st.subheader.write("FREE:")
  #st.write(response_Fjson)
  
  #with col2:
    #st.subheader.write("QUOTE:")
  st.header(symbol)
  st.subheader(response_Qjson)
  
  #st.line_chart(response_Cjson)
  
  

#if screen == 'Fundamentals':
#pass

# Free IEX price for AMC
#https://cloud.iexapis.com/stable/tops?token=YOUR_TOKEN_HERE&symbols=amc
#Stock quote for AMC
#https://cloud.iexapis.com/stable/stock/amc/quote?token=YOUR_TOKEN_HERE
