import guesser


def main():
    print("Добро пожаловать в игру 'угадай число'!")
    target: int = int(input("Загадайте целое число и введите его: "))
    print(
    """\
    Придумайте массив целых чисел, среди которых предположительн \
    может быть загаданное числа. Перечислите его элементы через пробел: \
    """
    )
    elements: list[int] = [int(i) for i in input().split(" ")]
    res = guesser.Guesser.guess(target, elements)
    print(f"Программа угадала число {res[0]} с {res[1]} раза")


if __name__ == "__main__":
    main()