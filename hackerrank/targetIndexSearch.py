def binarySearch(nums, target):
    return nums.index(target) if target in nums else -1
    
print(binarySearch([-1,0,3,5,9,12], 9)) # expected output: 4
print(binarySearch([2, 4, 6, 8, 10, 12, 14, 16], 16)) # expected output: 7
print(binarySearch([0], 5)) # expected output: -1
print(binarySearch([1, 10], 10)) # expected output: 0
