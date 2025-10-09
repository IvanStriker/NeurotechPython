import guesser

Outputs = {
    "hello":
        "Добро пожаловать в игру 'угадай число'!",
    "generate a number":
        "Загадайте целое число и введите его: ",
    "array form":
        "Придумайте массив целых чисел, среди которых "
        "предположительно может быть загаданное число.\n"
        "Если Вы хотите задать этот массив перечислением "
        "Всех элементов, введите 1.\n"
        "Если Вы хотите задать массив, как множество всех "
        "целых чисел,\n"
        "принадлежащих отрезку [a, b], перечислив "
        "лишь a и b, введите 2.\n",
    "each elem for array":
        "Перечислите элементы массива через пробел:\n",
    "enter a":
        "Введите a: ",
    "enter b":
        "Введите b: ",
    "type of algo":
        "Программа должна использовать двоичный поиск (1) "
        "или линейный поиск (2), чтобы угодать число?\n",
    "guessed":
        "Программа угадала число {num} с {trials} раза",
    "absent":
        "Программа поняла, что числа {num} нет в массиве, с {trials} раза"
}


def main():
    """
    This function realizes the game 'guess the number'
    between a user and the program.

    It asks user to guess the number and enter some
    other parameters to set the rules of the game. It
    prints out the amount of steps the algorithm made to
    guess the target number.
    """
    print(Outputs["hello"])
    target: int = int(input(Outputs["generate a number"]))

    arrayForm: int = int(input(Outputs["array form"]))
    if arrayForm == 1:
        elements: list[int] = [int(i) for i in input(
            Outputs["each elem for array"]).split(" ")]
    else:
        elements: list[int] = list(range(
            int(input(Outputs["enter a"])),
            int(input(Outputs["enter b"])) + 1
        ))

    algo = int(input(Outputs["type of algo"]))
    algo = {1: "bin", 2: "lin"}[algo]

    res = guesser.Guesser.guess(target, elements, algo)
    if res[0] is None:
        print(Outputs["absent"].format(num=target, trials=res[1]))
    else:
        print(Outputs["guessed"].format(num=res[0], trials=res[1]))


if __name__ == "__main__":
    main()
