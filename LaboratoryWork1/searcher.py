class SearcherInputTypeError(Exception):
    RESULTS = {2: "nums must be a list, but it isn't", 3: "target must be an int, but it isn't",
               4: "nums must consist of ints, but it doesn't"}

    def __init__(self, nums, target):
        self.message = "\n".join(
            [SearcherInputTypeError.RESULTS[i] for i in SearcherInputTypeError.checkTypes(nums, target)])

    def haveAnError(self):
        return bool(self.message)

    def __str__(self):
        return self.message

    @staticmethod
    def checkTypes(nums, target):
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
    def __init__(self, nums, target):
        self.message = "nums consists of less than 2 elems" if len(nums) < 2 else ""

    def haveAnError(self):
        return bool(self.message)

    def __str__(self):
        return self.message


class Searcher:
    @staticmethod
    def searchTwoWithSum(nums, target, noexcept=False):
        if not Searcher.__checkInput__(nums, target, SearcherInputTypeError, noexcept) \
                or not Searcher.__checkInput__(nums, target, SearcherInputValueError, noexcept):
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
