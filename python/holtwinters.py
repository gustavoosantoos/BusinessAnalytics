import pandas as pd
from datetime import datetime 
from item import Item
from mathutils import Math

class HoltWinters:
    __alfa__ = 0.8
    __beta__ = 0.8
    __gama__ = 0.8

    def __init__(self, itens, tamanhoPeriodo = 3):
        self.itens = itens
        self.__tamanhoPeriodo__ = tamanhoPeriodo

    def __setup__(self): 
        primeiroPeriodo = self.itens[0:self.__tamanhoPeriodo__]
        mediaValorPeriodo = Math.avg(lambda v: v.valor, primeiroPeriodo)
        for item in primeiroPeriodo:
            item.s = item.valor / mediaValorPeriodo
        
        ultimoItemPeriodo = primeiroPeriodo[-1]
        ultimoItemPeriodo.l = mediaValorPeriodo
        ultimoItemPeriodo.b = Math.extremesAvg(lambda v: v.valor, primeiroPeriodo)

    def __calculate__(self):
        print('')

    def __forecast__(self):
        print('')

    def calculate(self, numeroPrevisoes):
        self.__setup__()
        self.__calculate__()
        self.__forecast__()
        return self.itens

    @staticmethod
    def fromcsv(filePath, tamanhoPeriodo):
        data = pd.read_csv(filePath, sep = ';')
        data = map(lambda i: Item(datetime.strptime(i[0], '%d/%m/%Y'), i[1]), data.values.tolist())
        data = list(data)
        data.sort(key= lambda x: x.data)
        return HoltWinters(data, tamanhoPeriodo)