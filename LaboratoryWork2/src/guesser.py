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
                numbers. If method == "bin", it uses binary search,
                otherwise, linear algorithm is used. It's set to
                "bin" by default.

        Returns:
            tuple[int | None, int]: A tuple consisting of
                the number guessed and the amount of trials.
                The first value of tuple is equal to None only
                if target is not in elements.
        """
        Guesser._checkInput(target, elements)
        if len(elements) == 0:
            return None, 0
        elements.sort()
        if method == "bin":
            return Guesser._guessInLogTime(target, elements)
        else:
            return Guesser._guessInLinTime(target, elements)

    @staticmethod
    def _checkInput(target: int,
                    elements: list[int]):
        """
        This static function checks the types of Guesser.guess's params

        Raises:
            TypeError: if the types of the params don't match
                the signature
        """
        e = TypeError(
                "Parameters of wrong types for Guesser.guess.\n"
                "They must match the pattern:\n"
                "   target: int\n"
                "   elements: list[int]."
        )
        if not (isinstance(target, int) and
            isinstance(elements, list)):
            raise e
        for elem in elements:
            if not isinstance(elem, int):
                raise e

    @staticmethod
    def _guessInLinTime(target: int,
                        elements: list[int]
                        ) -> tuple[int | None, int]:
        """
        Realization for Guesser.guess in linear time.

        For in-class use only.

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

        For in-class use only.

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
        while leftBound < rightBound - 1:
            midIndex = (leftBound + rightBound) // 2
            midNumber = elements[midIndex]
            trials += 1
            if midNumber < target:
                leftBound = midIndex
            elif midNumber > target:
                rightBound = midIndex
            else:
                leftBound = midIndex - 1
                rightBound = midIndex + 1
                break
        if leftBound + 1 >= rightBound or elements[leftBound + 1] != target:
            return None, trials
        else:
            return target, trials
