def searchingTwo(nums: list[int], target: int):
    fstAcc = {}
    for i in range(len(nums)):
        if nums[i] in fstAcc:
            fstAcc[nums[i]] += [i]
        else:
            fstAcc[nums[i]] = [i]
    for i in range(len(nums)):
        if (target - nums[i]) in fstAcc:
            indexes = fstAcc[target - nums[i]]
            if indexes[0] != i:
                return [i, indexes[0]]
            elif len(indexes) > 1:
                return [i, indexes[1]]

    return None
