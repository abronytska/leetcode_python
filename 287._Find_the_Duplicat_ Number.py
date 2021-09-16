def findDuplicate(nums):
    # dic = {n: 0 for n in set(nums)}
    # for i in range(len(nums)):
    #     dic[nums[i]] += 1
    #     if dic[nums[i]] > 1:
    #         return nums[i]

    dic = {}
    for i in range(len(nums)):
        dic[nums[i]] = dic.get(nums[i], 0) + 1
        if dic[nums[i]] > 1:
            return nums[i] 

nums = [0, 2, 3, 3, 4]
print(findDuplicate(nums))


nums = [0, 1, 4, 4]
print(findDuplicate(nums))


nums = [6, 4, 2, 1, 4, 3, 5]
print(findDuplicate(nums))


nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))
