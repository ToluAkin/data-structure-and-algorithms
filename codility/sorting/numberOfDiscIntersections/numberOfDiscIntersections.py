def solution(A):
    lenA = len(A)
    leftValues = []
    rightValues = []
    index = 0
    open = 0
    intersect = 0
    position = 0
            
    for i in range(lenA):
        leftValues.append(i - A[i])
        rightValues.append(i + A[i])

    leftValues.sort()
    rightValues.sort()

    while position < len(leftValues):
        if leftValues[position] <= rightValues[index]:
            intersect += open
            open += 1
            position += 1
        else:
            open -= 1
            index += 1
        
        if intersect > 10000000:
            return -1
    return intersect
# print(solution([1, 5, 2, 1, 4, 0]))
print(solution([1, 5, 8, 7, 8, 4, 8, 5, 0, 5]))
print(solution([1, 0, 1, 0, 1]))
