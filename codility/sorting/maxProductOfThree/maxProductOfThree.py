def solution(A):
    A.sort()

    lastValues = A[-1] * A[-2] * A[-3]
    firstValues = A[0] * A[1] * A[-1]

    if lastValues > firstValues:
        maxValues = lastValues
    else:
        maxValues = firstValues
    return maxValues
print(solution([-3, 1, 2, -2, 5, 6]))
print(solution([-5, 5, -5, 4]))