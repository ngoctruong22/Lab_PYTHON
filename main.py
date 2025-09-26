def twoSum(nums, target):
    # push github
    if not nums:
        return None
    if not all(isinstance(num, int) for num in nums):
        return None
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None
