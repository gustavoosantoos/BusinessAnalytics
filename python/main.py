from holtwinters import HoltWinters

calc = HoltWinters.fromcsv('./sp500input.csv', 90)
itens = calc.calculate(0) 