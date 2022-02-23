def longestSubSeq(A):
    A.sort()
    count = 1
    previous = 0

    for index in range(1, len(A)):
        if A[index] - A[index - 1] == 1:
            count += 1
        else:
            if count > previous:
                previous = count
            count = 0

    return previous
print(longestSubSeq([1, 9, 87, 3, 10, 4, 20, 2, 45]))
print(longestSubSeq([36, 41, 56, 35, 91, 33, 34, 92, 43, 37, 42]))
