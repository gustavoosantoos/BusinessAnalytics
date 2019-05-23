from functools import reduce

class Math:
    @staticmethod
    def avg(selector, arr):
        arr = list(map(lambda i: selector(i), arr))
        return reduce(lambda a, b: a + b, arr) / len(arr)