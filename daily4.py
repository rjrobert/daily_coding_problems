"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def find_missing_int(nums):
    # max_num = max(nums)
    # if max_num <= 0:
    #     return -1

    for i in range(1, len(nums) + 2):
        if i not in nums:
            return i

    return -1


input1 = [3, 4, -1, 1]
input2 = [1, 2, 0]

print(find_missing_int(input1))
print(find_missing_int(input2))
