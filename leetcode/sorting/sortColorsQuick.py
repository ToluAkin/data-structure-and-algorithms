def sortColors(nums):
    lenNums = len(nums)
    
    if lenNums <= 1:
        return nums

    lessThan = []
    greaterThan = []
    pivot = nums[0]
    
    for element in nums[1:]:
        if element < pivot:
            lessThan.append(element)
        else:
            greaterThan.append(element)
    print(lessThan, greaterThan, pivot)
    return sortColors(lessThan) + [pivot] + sortColors(greaterThan)

    # lenNums = len(nums)

    # if lenNums <= 1:
    #     return nums

    # left = 0
    # right = lenNums - 1
    # i = 0

    # while i <= right:
    #     if nums[i] == 0:
    #         nums[i], nums[left] = nums[left], nums[i]
    #         left += 1
    #     elif nums[i] == 2:
    #         nums[i], nums[right] = nums[right], nums[i]
    #         right -= 1
    #         i -= 1

    #     i += 1
    # return nums
print(sortColors([2,0,2,1,1,0]))