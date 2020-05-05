"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def max_sum(nums):
    curr_len = len(nums)
    maxNums = [0] * curr_len
    maxNum = 0
    i = curr_len - 1
    while i > 0:
        maxNums[i] = max_sum_helper(nums, i, maxNum, maxNums)
        maxNum = max(maxNum, maxNums[i])
        i -= 1
    return maxNum


def max_sum_helper(nums, curr_idx, curr_len, maxNums):
    if maxNums[curr_idx] != 0:
        return maxNums[curr_idx]
    if curr_idx in [0, 1]:
        return nums[curr_idx]
    if curr_idx - 2 == 0:
        return nums[curr_idx] + max_sum_helper(nums, curr_idx - 2, curr_len, maxNums)

    return nums[curr_idx] + max(max_sum_helper(nums, curr_idx - 2, curr_len, maxNums),
                                max_sum_helper(nums, curr_idx - 2, curr_len, maxNums))


nums = [2, 4, 6, 2, 5]
print(max_sum(nums))
