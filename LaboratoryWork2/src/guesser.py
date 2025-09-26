class Guesser:
    """
    This is the main class. Its static method guess realizes
    the algorithm from TO DO.
    """

    @staticmethod
    def guess(target: int,
              elements: list[int],
              method: str = "bin") -> tuple[int | None, int]:
        """
        This static function tries to guess the target number.
        It "knows" only the range that contains the number needed.
        The function uses linear algorithm or binary search based on
        "method" argument.

        Args:
            target (int): The number to guess
            elements (list[int]): The elements defining the field of
                search for target.
            method (str): The algorithm used in function to guess
                numbers. If method = "bin", it uses binary search,
                otherwise, linear algorithm is used. It's set to
                "bin" by default.

        Returns:
            tuple[int | None, int]: A tuple consisting of
                the number guessed and the amount of trials.
                The first value of tuple is equal to None only
                if target is not in elements.
        """
        if len(elements) == 0:
            return None, 0
        elements.sort()
        if method == "bin":
            return Guesser._guessInLogTime(target, elements)
        else:
            return Guesser._guessInLinTime(target, elements)

    @staticmethod
    def _guessInLinTime(target: int,
                        elements: list[int]
                        ) -> tuple[int | None, int]:
        """
        Realization for Guesser.guess in linear time.
        For in-class use onle.

        Args:
            target (int): The number to guess
            elements (list[int]): The field of searching for target

        Returns:
            tuple[int | None, int]: A tuple consisting of
                the number guessed and the amount of trials.
                The first value of tuple is equal to None only
                if target is not in elements.

        """
        for current in range(len(elements)):
            if elements[current] == target:
                return elements[current], current + 1
        return None, len(elements)

    @staticmethod
    def _guessInLogTime(target: int,
                        elements: list[int]
                        ) -> tuple[int | None, int]:
        """
        Realization for Guesser.guess in logarithmic time.
        For in-class use onle.

        Args:
            target (int): The number to guess
            elements (list[int]): The field of searching for target

        Returns:
            tuple[int | None, int]: A tuple consisting of
                the number guessed and the amount of trials.
                The first value of tuple is equal to None only
                if target is not in elements.

        """
        leftBound = -1
        rightBound = len(elements)
        trials = 0
        print(*elements)
        while leftBound < rightBound - 1:
            midIndex = (leftBound + rightBound) // 2
            midNumber = elements[midIndex]
            trials += 1
            print(midIndex, end=" ")
            if midNumber < target:
                leftBound = midIndex
            elif midNumber > target:
                rightBound = midIndex
            else:
                leftBound = midIndex - 1
                rightBound = midIndex + 1
                break
        result = elements[leftBound + 1]
        print()
        if result == target:
            return target, trials
        else:
            return None, trials