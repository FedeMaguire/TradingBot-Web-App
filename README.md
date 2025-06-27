# TradingBot-Web-App
# BINANCE Trading Bot with WEB APP Live Dashboard.
## This is a real-time Binance Trading Bot developed in Python. It streams its performance live to a Flask-based web app, providing real-time updates on trading activity, performance metrics, trading cycle charts, and overall system status.
![image](https://github.com/FedeMaguire/TradingBot-Web-App/blob/main/final%20images/full.jpg?raw=true)

# Trading Bot and Web Dashboard Overview
# How it Works
This system is a real-time cryptocurrency trading bot developed in Python, integrated with a live web dashboard built using Flask and HTML. It continuously retrieves market data from Binance through its official API, monitors price action and technical indicators, and automatically places trades based on a predefined strategy—specifically, a triple EMA crossover. 
All trading activity, performance metrics, and live analysis are streamed to a Flask-based web app, creating a dynamic and transparent Performance Dashboard.
This setup enables transparent monitoring of live trades and automated strategy performance.
# 
- Status bar:
![image](https://github.com/FedeMaguire/TradingBot-Web-App/blob/main/final%20images/status.jpg?raw=true)
# 
- Performance of the current trade cycle:
![image](https://github.com/FedeMaguire/TradingBot-Web-App/blob/main/final%20images/performance.jpg?raw=true)
# 
- Current trade chart:
![image](https://github.com/FedeMaguire/TradingBot-Web-App/blob/main/final%20images/trade_no_info.jpg?raw=true)
# 
- Live chart of the last 2 hours of Bitcoin price action:
![image](https://github.com/FedeMaguire/TradingBot-Web-App/blob/main/final%20images/BTC_2_hours.jpg?raw=true)
# 
- Full-cycle chart showing BTC price movement throughout the trade
![image](https://github.com/FedeMaguire/TradingBot-Web-App/blob/main/final%20images/btc_cycle.jpg?raw=true)
# 
- Dynamic data table showing the last 20 data points used in the analysis:
![image](https://github.com/FedeMaguire/TradingBot-Web-App/blob/main/final%20images/dataframe.jpg?raw=true)
# 
All charts include interactive hover details.
![image](https://github.com/FedeMaguire/TradingBot-Web-App/blob/main/final%20images/hover_info.jpg?raw=true)
![image](https://github.com/FedeMaguire/TradingBot-Web-App/blob/main/final%20images/trade.jpg?raw=true)
#
- # Libraries
```
from flask import Flask, render_template
import pandas as pd
import os
import ta #Tecnical indicators
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import traceback
from datetime import datetime, timedelta
import threading
import subprocess
import time
import requests
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
- # Libraries:
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```


# Disclaimer
This project is for informational purposes only. It is not legal, tax, investment, financial, or other advice. Nothing contained here constitutes a solicitation, recommendation, endorsement, or offer to buy or sell any securities or other financial instruments in any jurisdiction. Use at your own risk.

Under no circumstances will I be held responsible or liable in any way for any claims, damages, losses, expenses, costs, or liabilities whatsoever, including, without limitation, any direct or indirect damages for loss of profits.
