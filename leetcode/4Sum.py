def fourSum(nums, target):
    lenArray = len(nums)

    if lenArray < 4:
        return []

    nums.sort()
    distinct = {}

    for i in range(lenArray - 3):
        for j in range(i + 1, lenArray - 2):
            startSum = nums[i] + nums[j]
            left = j + 1
            right = lenArray - 1

            while left < right:
                endSum = startSum + nums[left] + nums[right]

                if endSum == target:
                    distinct[nums[i], nums[j], nums[left], nums[right]] = i
                    left += 1
                    right -= 1
                elif endSum < target:
                    left += 1
                else:
                    right -= 1
    print(distinct.keys())
    return distinct.keys()
print(fourSum([1, 0, -1, 0, -2, 2], 0))
print(fourSum([2, 2, 2, 2, 2], 8))