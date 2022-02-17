def solution(N, A):
    startArray = [0] * N
    counterX = 0
    maxNumber = 0

    for index in range(len(A)):
        if A[index] == N + 1:
            maxNumber = counterX
        else:
            if startArray[A[index] - 1] < maxNumber:
                startArray[A[index] - 1] += (maxNumber - startArray[A[index] - 1])
        
            startArray[A[index] - 1] += 1
            
            if startArray[A[index] - 1] > counterX:
                counterX = startArray[A[index] - 1]
    
    for i in range(N):
        if startArray[i] < maxNumber:
            startArray[i] += (maxNumber - startArray[i])
    #print(startArray)
    return startArray
solution(1, [2, 1, 1, 2, 1])
solution(5, [3, 4, 4, 6, 1, 4, 4])