import pandas as pd
import datetime
from item import Item
from functools import reduce

class HoltWinters:
    __alfa__ = 0.8
    __beta__ = 0.8
    __gama__ = 0.8

    def __init__(self, itens, tamanhoPeriodo = 3):
        self.itens = itens
        self.__tamanhoPeriodo__ = tamanhoPeriodo

    def __setup__(self): 
        primeiroPeriodo = self.itens[0:self.__tamanhoPeriodo__]
        for item in primeiroPeriodo:
            item.s = item.valor / (reduce(lambda a, b: a + b.valor, primeiroPeriodo, 0) / self.__tamanhoPeriodo__)

    def calculate(self, numeroPrevisoes):
        self.__setup__()

    @staticmethod
    def fromcsv(filePath, tamanhoPeriodo):
        data = pd.read_csv(filePath, sep = ';')
        data = map(lambda i: Item(datetime.datetime.strptime(i[0], '%d/%m/%Y'), i[1]), data.values.tolist())
        data = list(data)
        data.sort(key= lambda x: x.data)
        return HoltWinters(data, tamanhoPeriodo)
