def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        
        if nums[left] < nums[mid]:
            if target < nums[left] or target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target > nums[right] or target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1
print(search([4,5,6,7,0,1,2], 2))