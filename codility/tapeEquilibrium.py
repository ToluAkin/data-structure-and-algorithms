import sys

def solution(A):
    lowest = sys.maxsize
    sumA = sum(A)
    point1 = 0
    point2 = 0
    print(lowest)
    for i in range(len(A) - 1):
        point1 += A[i]
        point2 = sumA - point1
        value = abs(point1 - point2)

        if value < lowest:
            lowest = value
    print(lowest)
solution([3, 1, 2, 4, 3])