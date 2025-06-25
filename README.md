# TradingBot-Web-App
# BINANCE Trading Bot with WEB APP Live Dashboard.
![image](https://github.com/FedeMaguire/TradingBot-Web-App/blob/main/final%20images/full_view.jpg?raw=true)
# Trading Bot and Web Dashboard Overview
## This is a real-time Binance Trading Bot developed in Python. It streams its performance live to a Flask-based web app, providing real-time updates on trading activity, performance metrics, trading cycle charts, and overall system status.
![image](https://github.com/FedeMaguire/TradingBot-Web-App/blob/main/final%20images/status.jpg?raw=true)
 # 
![image](https://github.com/FedeMaguire/TradingBot-Web-App/blob/main/final%20images/performance.jpg?raw=true)

# How it Works
This system is a real-time cryptocurrency trading bot codedmin python integrated with a live web dashboard using Flask and HTML. Market data is continuously fetched from Binance via its official API. The bot monitors price action and technical indicators, and automatically places trades when a predefined condition—specifically, a triple EMA crossover—is detected .All trading activity and live analysis are streamed to a Flask-based web app to create Peeformance Dashboard.
# Graphical User Interface

All trading activity and live analysis are streamed to a Flask-based web app, which displays:
-The performance of the current trade cycle
# 
![image](https://github.com/FedeMaguire/Python-Trading-Bot/blob/main/screenshots/Screenshot%202023-11-09%20165322.jpg?raw=true)
# 

-A live chart of the last 2 hours of Bitcoin price action

-A full-cycle chart showing BTC price movement throughout the trade

-A dynamic data table showing the last 20 data points used in the analysis

This setup enables transparent monitoring of live trades and automated strategy performance.
- # Libraries
```
import customtkinter
import os
from PIL import Image
import pandas as pd
import plotly.graph_objects as go
```
 

# Prerequisites
- Binance API key (stored in "keys.py")
- Binance API secret (stored in "keys.py")

# TradingBot
- # Libraries
```
import pandas as pd
import ta #Tecnical indicators
from binance import Client
from datetime import timedelta # Add and substract timestamps
import time
from pytz import timezone
from keys import api_key, api_secret
```
# Charts:
The charts are created using the matplotlib and mplfinance libraries and loaded to the GUI as JPG files every time a new event is scheduled.
- # Libraries:
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf
```


# Disclaimer
This project is for informational purposes only. It is not legal, tax, investment, financial, or other advice. Nothing contained here constitutes a solicitation, recommendation, endorsement, or offer to buy or sell any securities or other financial instruments in any jurisdiction. Use at your own risk.

Under no circumstances will I be held responsible or liable in any way for any claims, damages, losses, expenses, costs, or liabilities whatsoever, including, without limitation, any direct or indirect damages for loss of profits.
