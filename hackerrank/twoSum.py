def findTaskPairForSlot(taskDurations, slotLength):
    # Write your code here
    # return the indices of two elements that sum to the target or [-1, -1] if no such pair exists
    if len(taskDurations) < 2:
        return [-1, -1]
    
    left = 0
    right = 1
    while left < right:
        if taskDurations[left] + taskDurations[right] == slotLength:
            print([left, right])
            return [left, right]
        elif taskDurations[left] + taskDurations[right] < slotLength and right < len(taskDurations) - 1:
            right += 1
        elif left != len(taskDurations) - 2 and right == len(taskDurations) - 1:
            left += 1
            right = left + 1
        else:
            print([-1, -1])
            return [-1, -1]
    
    print([-1, -1])
    return [-1, -1]

# Example test cases
# findTaskPairForSlot([30, 20, 150, 100, 40], 90)  # expected output: [-1, -1]
# findTaskPairForSlot([2, 7, 11, 15], 9)  # expected output: [0, 1]
# findTaskPairForSlot([1, 2, 3, 4], 8)  # expected output: [-1, -1]
# findTaskPairForSlot([1, 3, 4, 5, 7, 10, 11], 15)  # expected output: [2, 6]
# findTaskPairForSlot([], 10)  # expected output: [-1, -1]
# findTaskPairForSlot([5], 10)  # expected output: [-1, -1]