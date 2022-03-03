def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        sumUp = numbers[left] + numbers[right]

        if sumUp == target:
            return [left+1, right+1]
        elif sumUp > target:
            right -= 1
        else:
            left += 1

print(twoSum([2, 7, 11, 15]))
print(twoSum([2,3,4]))
