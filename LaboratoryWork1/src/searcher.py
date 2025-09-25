class SearcherInputTypeError(Exception):
    """A class describing errors raised when you put arguments of
    wrong type to Searcher.searchTwoWithSum method.

    Attributes:
        RESULTS (Dict[int, str]): A static variable. It defines
            all the possible messages you can see when an error raised
    """

    RESULTS = {2: "nums must be a list, but it isn't",
               3: "target must be an int, but it isn't",
               4: "nums must consist of ints, but it doesn't"}

    def __init__(self, nums, target):
        """Constructs an error object based on whether arguments are
        of the valid types or not.

        Args:
            nums (List[int])
            target (int)
        """
        self.message = "\n".join(
            [SearcherInputTypeError.RESULTS[i]
             for i in SearcherInputTypeError.__checkTypes__(nums, target)])

    def haveAnError(self):
        """Returns if the arguments given to the constructor are valid.
        In other words, it tells you whether you need to rais this error
        or not.

        Returns:
            bool: value showing if current error message isn't empty
        """
        return bool(self.message)

    def __str__(self):
        """Required error's method.

        Returns:
            str: message explaining error's reasons
        """
        return self.message

    @staticmethod
    def __checkTypes__(nums, target):
        """This method forms an array of error messages based on
        the arguments given realizing the logic of the constructor.
        It's for in-class use only.

        Args:
            nums (List[int])
            target (int)

        Returns:
            List[str]: error messages
        """
        res = []
        if not isinstance(nums, list):
            res += [2]
        if not isinstance(target, int):
            res += [3]
        for i in nums:
            if not isinstance(i, int):
                res += [4]
                break
        return res


class SearcherInputValueError(Exception):
    """A class describing errors raised when you put arguments of
    wrong value to Searcher.searchTwoWithSum method."""
    def __init__(self, nums, target):
        """Constructs an error object based on whether arguments are
        of valid values or not.

        Args:
            nums (List[int])
            target (int)
        """
        self.message = "nums consists of less than 2 elems" \
            if len(nums) < 2 else ""

    def haveAnError(self):
        """Returns if the arguments given to the constructor are valid.
        In other words, it tells you whether you need to rais this error
        or not.

        Returns:
            bool: value showing if current error message isn't empty
        """
        return bool(self.message)

    def __str__(self):
        """Required error's method.

        Returns:
            str: message explaining error's reasons
        """
        return self.message


class Searcher:
    """This class includes program's main algorithm."""
    @staticmethod
    def searchTwoWithSum(nums, target, noexcept=False):
        """This method finds two numbers of sum 'target' in 'nums' list
        in linear time. If there is more than one combination
        providing with the sum needed, the algorithm will return
        the least in lexicographic order list of two indexes.

        Args:
            nums (List[int]): The field for search
            target (int): The sum needed
            noexcept (bool): If True, the method will return None in
                case of any errors raised. False by default

        Raises:
            SearcherInputTypeError: Warns if the arguments are of invalid types.
            SearcherInputValueError: Warns if len(nums) < 2.

        Returns:
            List[int]: The found two numbers of 'target' sum from 'nums'.
        """
        if any([not Searcher.__checkInput__(nums, target, i, noexcept)
                for i in [SearcherInputTypeError,
                          SearcherInputValueError]]):
            return None
        fstAcc = {}
        for i in range(len(nums)):
            fstAcc.setdefault(nums[i], []).append(i)
        for i in range(len(nums)):
            if (target - nums[i]) in fstAcc:
                indexes = fstAcc[target - nums[i]]
                if indexes[0] != i:
                    return [i, indexes[0]]
                elif len(indexes) > 1:
                    return [i, indexes[1]]
        return None

    @staticmethod
    def __checkInput__(nums, target, classType, noexcept):
        if (error := classType(nums, target)).haveAnError():
            if noexcept:
                return False
            else:
                raise error
        return True
