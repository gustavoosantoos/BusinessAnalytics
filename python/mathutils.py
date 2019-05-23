from functools import reduce

class Math:
    @staticmethod
    def avg(selector, arr):
        arr = list(map(lambda i: selector(i), arr))
        return reduce(lambda a, b: a + b, arr) / len(arr)

    @staticmethod
    def extremesAvg(selector, arr):
        arr = list(map(lambda i: selector(i), arr))
        sum = 0
        for i in range(0, int(len(arr) / 2)):
            sum += (arr[i] + arr[len(arr) - (i + 1)]) / 2
        return sum / len(arr)