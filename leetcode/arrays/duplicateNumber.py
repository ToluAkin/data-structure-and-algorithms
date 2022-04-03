def findDuplicate(nums):
    new_dict = {}

    for num in nums:
        if num in new_dict:
            return num
        else:
            new_dict[num] = num

print(findDuplicate([1, 3, 4, 2, 2]))
print(findDuplicate([3, 1, 3, 4, 2]))
