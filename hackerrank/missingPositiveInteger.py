def findSmallestMissingPositive(orderNumbers):
    # Write your code here
    n = len(orderNumbers)
    for i in range(n):
        while 1 <= orderNumbers[i] <= n and orderNumbers[orderNumbers[i] - 1] != orderNumbers[i]:
            correct_idx = orderNumbers[i] - 1
            orderNumbers[i], orderNumbers[correct_idx] = orderNumbers[correct_idx], orderNumbers[i]

    for i in range(n):
        if orderNumbers[i] != i + 1:
            print(i + 1)
            return i + 1
    print(n + 1)
    return n + 1

# Example test cases
# findSmallestMissingPositive([0, 0, -1, 1, 2, 3, 3, 3, 4]) # expected output 5
# findSmallestMissingPositive([3, 4, -1, 1])  # expected output 2
# findSmallestMissingPositive([1, 2, 0]) # expected output 3
findSmallestMissingPositive([7, 8, 9, 11, 12]) # expected output 1
# findSmallestMissingPositive([-1, -2, -3]) # expected output 1
# findSmallestMissingPositive([1, 2, 3, 4, 5]) # expected output 6
# findSmallestMissingPositive([-4, -5, 1, 1]) # expected output 2
# findSmallestMissingPositive([5, 0, 0, -1, -2])  # expected output 1
# findSmallestMissingPositive([])  # expected output 1
# findSmallestMissingPositive([2])  # expected output 1
# findSmallestMissingPositive([1])  # expected output 2