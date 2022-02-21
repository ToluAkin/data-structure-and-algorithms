# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    stroke = 0
    sum = 0

    for value in A:
        if value < stroke:
            sum += (stroke - value)
        stroke = value
    sum += stroke
    return sum
# [1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]
# [5, 8]
# [1, 1, 1, 1]