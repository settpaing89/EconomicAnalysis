import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries

# Alpha Vantage API key
api_key = 'HCJK797OY6V1U9E0'

# Initialize TimeSeries object
ts = TimeSeries(key=api_key, output_format='pandas')

# Fetch daily stock prices for S&P 500 (symbol: SPY)
data, meta_data = ts.get_daily(symbol='SPY', outputsize='full')

# Preprocessing: sort data by date
data = data.sort_index()

# Rename columns for easier access
data.rename(columns={
    '1. open': 'open',
    '2. high': 'high',
    '3. low': 'low',
    '4. close': 'close',
    '5. volume': 'volume'
}, inplace=True)

# Save the preprocessed data
data.to_csv('sp500_daily.csv')

# Display the first few rows of the dataset
data.head()
