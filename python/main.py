from holtwinters import HoltWinters

calc = HoltWinters.fromcsv('./sp500input.csv', 90)
itens = calc.calculate(0) 
item = itens[89]
print(str(item.data) + " - " + str(item.valor) + " - " + str(item.l) + " - " + str(item.b) + " - " + str(item.s))