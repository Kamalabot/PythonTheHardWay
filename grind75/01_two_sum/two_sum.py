from typing import List

ProblemStatement = """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""
link = "https://leetcode.com/problems/two-sum/description/"
solution = "accepted"

def two_sum(nums: List, target: int) -> List:
    # check if nums list is meeting the constraints
    if len(nums) < 2 or len(nums) > 10 ** 4: 
        raise ValueError("The length of nums is out of range")
    if target < 10e-9 or target > 10e9:
        raise ValueError("target is out of range")
    # enumerate over the length of nums by creating a range,
    for i in range(len(nums)):
        # take value at num[i] and assign it to temp
        temp = nums[i]
        # enumerate over the remaining part of the nums
        for x, ele in enumerate(nums):
            # skip the index that is refered by 'i' 
            if x != i:
                # check if sum of value at i and x is equal to target
                if ele + temp == target:
                    return [i, x]


nums = [2, 7, 11, 15]
target = 9
assert two_sum(nums, target) == [0, 1]

nums = [3, 2, 4]
target = 6
assert two_sum(nums, target) == [1, 2]

nums = [3, 3]
target = 6
assert two_sum(nums, target) == [0, 1]

nums = list(range(10 ** 5))
target = 5
# assert two_sum(nums, target) == [2, 3]

nums = list(range(10))
target = 10e9 + 1
# assert two_sum(nums, target) == [2, 3]
