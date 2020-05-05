"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def array_product(nums):
    retVal = []
    totalVal = total_product(nums)

    for i in range(0, len(nums)):
        retVal.append(totalVal / nums[i])

    return retVal


def array_product2(nums):
    retVal = []

    for i in range(0, len(nums)):
        tempNums = list(nums)
        tempNums.pop(i)
        tempVal = total_product(tempNums)
        retVal.append(tempVal)

    return retVal


def total_product(nums):
    totalVal = 1
    for i in range(0, len(nums)):
        totalVal = totalVal * nums[i]

    return totalVal


nums = [1, 2, 3, 4, 5]
print(array_product2(nums))

nums = [3, 2, 1]
print(array_product2(nums))
