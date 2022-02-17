def solution(A):
    A.sort()
    lenA = len(A)

    if A[-1] < 0:
        return 1

    if lenA == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    
    maxValue = max(A)
    newArray = [0] * maxValue

    for i in range(lenA):
        if A[i] > 0:
            if newArray[A[i] - 1] != 1:
                newArray[A[i] - 1] = 1
                print(newArray[A[i] - 1], newArray)
                
    
    for i in range(maxValue):
        if newArray[i] == 0:
            return i + 1
    return i + 2

solution([1, 3, 6, 4, 1, 2])
# solution([1, 2, 3])
# solution([-1, -3])