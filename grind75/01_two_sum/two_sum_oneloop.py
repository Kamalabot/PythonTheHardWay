from typing import List

ProblemStatement = """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""
link = "https://leetcode.com/problems/two-sum/description/"


# Implementing the dict solution for O(n) time complexity
def two_sum(nums, target):
    # store nums' element and its indices in dict 
    comp_dict = dict({num: ind for ind, num in enumerate(nums)})
    # print(comp_dict)
    # traverse the nums array
    for indx, num in enumerate(nums):
        # take the complement of num
        comp = target - num
        # check if comp in comp_dict
        if comp in comp_dict:
            # check if idx of complement
            # is not same as current index
            if indx != comp_dict[comp]:
                # return the indices
                return [indx, comp_dict[comp]]

    return []


nums = [2, 7, 11, 15]
target = 9
assert two_sum(nums, target) == [0, 1]

nums = [3, 2, 4]
target = 6
assert two_sum(nums, target) == [1, 2]

nums = [3, 3]
target = 6
assert two_sum(nums, target) == [0, 1]