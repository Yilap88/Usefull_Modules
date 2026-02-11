## module_ARIMA.py 
### This module runs an ARIMA model on the data and forecasts the next 12 periods. It also plots the results.

## Requirements:
### pandas, numpy, matplotlib, statsmodels

## Input:
### data: A pandas Series with the time series data, just 2 columns: 'Date' and 'Value'. The 'Date' column should be in datetime format and set as the index.

## Pipeline:




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from statsmodels.tsa.arima.model import ARIMA

data = pd.read_csv('test_data/IPC.csv')
print(data)

plt.plot(data['Meses'], data['Indice'])
plt.show()