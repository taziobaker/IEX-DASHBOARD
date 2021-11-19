import streamlit as st
import pandas as pd
import base64
#import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
#import yfinance as yf

def load_data():
  #url = f"https://cloud.iexapis.com/stable/stock/amc/chart/1d?token={config.sk_05f62d0b97b84cfbb15650bc980058b0}"
  url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
  hrml = pd.read_html(url, header = 0)
  df = html[0]
  return df

df = load_data()
df
