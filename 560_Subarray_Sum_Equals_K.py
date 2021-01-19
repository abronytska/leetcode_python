def subarraySum(nums, k):
    result, current_sum, sums = 0, 0, {}
    for num in nums:
        sums[current_sum] = sums.get(current_sum, 0) + 1
        current_sum += num
        if sums.get(current_sum - k):
            result += sums[current_sum - k]
    return result


print(subarraySum([1, 2, 3, 4], 3))
# print(subarraySum([1, 1, 1], 2))
# print(subarraySum([1, 2, 1, 2, 1], 3))
# print(subarraySum([1], 1))
# print(subarraySum([-1, -1, 1], 0)) #1
# print(subarraySum([-1, -1, 1], 1)) #1
# print(subarraySum([-1, -1, 1], -2)) #1
