from holtwinters import HoltWinters

calc = HoltWinters.fromcsv('./sp500input.csv', 90)
calc.calculate(0)