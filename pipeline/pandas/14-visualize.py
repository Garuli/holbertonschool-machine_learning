#!/usr/bin/env python3
"""Module that visualizes Bitcoin data."""
import matplotlib.pyplot as plt
import pandas as pd

from_file = __import__('2-from_file').from_file

# Load the Coinbase CSV into a DataFrame (',' is the column separator)
df = from_file(
    'coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ','
)

# drop(): remove the Weighted_Price column, it is not needed
df = df.drop(columns=['Weighted_Price'])

df = df.rename(columns={'Timestamp': 'Date'})

# to_datetime(): convert Unix seconds (e.g. 1417411980) to real dates
df['Date'] = pd.to_datetime(df['Date'], unit='s')

# set_index(): use the Date column as the row labels (needed to select by date and to resample by time)
df = df.set_index('Date')

df['Close'] = df['Close'].ffill()

for column in ['High', 'Low', 'Open']:
    df[column] = df[column].fillna(df['Close'])

for column in ['Volume_(BTC)', 'Volume_(Currency)']:
    df[column] = df[column].fillna(0)

# loc[]: select rows by label, '2017':  means from 2017 to the end
df = df.loc['2017':]

# resample('D'): group the 1-minute rows into one group per day
df = df.resample('D').agg({
    'High': 'max',                
    'Low': 'min',                 
    'Open': 'mean',               
    'Close': 'mean',              
    'Volume_(BTC)': 'sum',        
    'Volume_(Currency)': 'sum'    
})

print(df)

# plot(): draw one line per column, the index (Date) is the x axis
df.plot()

plt.show()