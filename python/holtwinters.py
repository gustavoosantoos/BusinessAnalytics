import pandas as pd
import datetime
from item import Item

class HoltWinters:
    def __init__(self, itens):
        self.itens = itens

    @staticmethod
    def fromcsv(filePath):
        data = pd.read_csv(filePath, sep = ';')
        data = map(lambda i: Item(datetime.datetime.strptime(i[0], '%d/%m/%Y'), i[1]), data.values.tolist())
        data = list(data)
        data.sort(key= lambda x: x.data)
        return HoltWinters(data)
