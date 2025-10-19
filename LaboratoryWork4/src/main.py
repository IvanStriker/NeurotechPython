import matplotlib.pyplot as plt
import random

from factorial_counter import FactorialCounter as FC


def main():
    random.seed(42)
    test_data = list(range(10, 300, 10))

    res_recursive = []
    res_iterative = []
    res_recursive_cached = []
    res_iterative_cached = []

    for n in test_data:
        res_recursive.append(FC.benchmark(FC.countRecursively, n,
                                          number=1000, repeat=5))
        res_iterative.append(FC.benchmark(FC.countIteratively, n,
                                          number=1000, repeat=5))
        res_recursive_cached.append(FC.benchmark(FC.countRecursivelyCached, n,
                                                 number=1000, repeat=5))
        res_iterative_cached.append(FC.benchmark(FC.countIterativelyCached, n,
                                                 number=1000, repeat=5))

    # Визуализация
    plt.figure(figsize=(15, 10))
    plt.subplot(1, 2, 1)
    plt.plot(test_data, res_recursive, label="Рекурсивный")
    plt.plot(test_data, res_iterative, label="Итеративный")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение рекурсивного и итеративного факториала")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(test_data, res_recursive_cached, label="Рекурсивный + кеш")
    plt.plot(test_data, res_iterative_cached, label="Итеративный + кеш")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение рекурсивного и итеративного факториала с хешами")
    plt.legend()
    plt.savefig("outputImage.png")


if __name__ == "__main__":
    main()
