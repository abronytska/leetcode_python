# def productExceptSelf(nums):
#     new_list = list()
#     for i in range(len(nums)):
#         temp_var = 1
#         for j in range(len(nums)):
#             if i != j:
#                 temp_var = temp_var * nums[j]
#         new_list.append(temp_var)
#     return new_list
#
#
# print(productExceptSelf([1, 2, 3, 4]))
# print(productExceptSelf([4, 5, 1, 8, 2]))


def productExceptSelf(nums):
    new_list = list()
    L = [1] * len(nums)
    R = [1] * len(nums)

    for i in range(len(nums) - 1):
        L[i + 1] = L[i] * nums[i]

    for i in range(len(nums) - 1, 0,  -1):
        R[i - 1] = R[i] * nums[i]

    for i in range(len(nums)):
        new_list.append(L[i] * R[i])

    return new_list


print(productExceptSelf([1, 2, 3, 4]))