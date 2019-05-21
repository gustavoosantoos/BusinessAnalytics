import pandas as pd 
import os

data = pd.read_csv('./sp500input.csv', sep = ';')

print(data.head())