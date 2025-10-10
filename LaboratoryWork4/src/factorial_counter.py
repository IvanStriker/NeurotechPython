import timeit
from functools import lru_cache
from functools import cache


class FactorialCounter:

    @staticmethod
    def countRecursively(number: int) -> int:
        if number == 0:
            return 1
        return number * FactorialCounter.countRecursively(number - 1)

    @staticmethod
    @lru_cache(maxsize=128)
    def countRecursivelyCached(number: int) -> int:
        if number == 0:
            return 1
        return number * FactorialCounter.countRecursivelyCached(number - 1)

    @staticmethod
    def countIteratively(number: int) -> int:
        res = 1
        for i in range(1, number + 1):
            res *= i
        return res

    @staticmethod
    @lru_cache(maxsize=128)
    def countIterativelyCached(number: int) -> int:
        res = 1
        for i in range(1, number + 1):
            res *= i
        return res

    @staticmethod
    def benchmark(func, data, number=1, repeat=5):
        """Возвращает среднее время выполнения func на наборе data"""
        times = timeit.repeat(lambda: func(data), number=number, repeat=repeat)
        return min(times)

