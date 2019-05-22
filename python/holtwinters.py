import pandas as pd 
import os
import datetime

class Item:
    def __init__(self, data, valor):
        self.data = data
        self.valor = valor

data = pd.read_csv('./sp500input.csv', sep = ';')
data = map(lambda i: Item(datetime.datetime.strptime(i[0], '%d/%m/%Y'), i[1]), data.values.tolist())
data = list(data)
data.sort(key= lambda x: x.data)

for index, row in enumerate(data):
    print(str(index) + " - " + str(row.data) + ": " + str(row.valor))