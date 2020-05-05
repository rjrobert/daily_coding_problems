def sum_in_list(nums, k):
    for i in range(0, len(nums)):
        if k > nums[i]:
            if (k - nums[i]) in nums:
                return True
    return False


nums = [1, 15, 3, 7, 10]

print(sum_in_list(nums, 17))
