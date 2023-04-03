import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns, numpy as np
import requests
import json

import plotly.graph_objects as go
from datetime import datetime

symbol="SPY"

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+symbol+'&interval=5min&apikey=AKCp8hzhKHWQDFeiF1nXFVgWaMdTxuMVQ7WpFo9'
k="Time Series (5min)"
ti="Daily"

r = requests.get(url)
data = r.json()
dates = data[k]

time=[]
high=[]
open=[]
close=[]
low=[]
volume=[]
for key, value in  dates.items():
        time.append(key)
        open.append(value["1. open"])
        high.append(value["2. high"])
        low.append(value["3. low"])
        close.append(value["4. close"])
        volume.append(value["5. volume"])

df = pd.DataFrame({"time":time, "open":open, "high":high, "low":low, "close":close})

print("df:", df)
fig = go.Figure(data=[go.Candlestick(x=df['time'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])],
                layout=go.Layout(
                title=go.layout.Title(text=symbol+" "+ti)
    ))

fig.show()
ti="Monthly"
url ='https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='+symbol+'&apikey=AKCp8hzhKHWQDFeiF1nXFVgWaMdTxuMVQ7WpFo9'
r = requests.get(url)
data = r.json()
k="Monthly Time Series"
dates = data[k]
time=[]
high=[]
open=[]
close=[]
low=[]
volume=[]
for key, value in  dates.items():
        time.append(key)
        open.append(value["1. open"])
        high.append(value["2. high"])
        low.append(value["3. low"])
        close.append(value["4. close"])
        volume.append(value["5. volume"])

df = pd.DataFrame({"time":time, "open":open, "high":high, "low":low, "close":close})

print("df:", df)
fig = go.Figure(data=[go.Candlestick(x=df['time'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])],
                layout=go.Layout(
                title=go.layout.Title(text=symbol+" "+ti)
    ))


fig.show()
