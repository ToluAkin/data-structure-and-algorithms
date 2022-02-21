def solution(A):
    lenA = len(A)
    leftValues = []
    rightValues = []
    count = 0
    index = 0
            
    for i in range(lenA):
        leftValues.append(i - A[i])
        rightValues.append(i + A[i])

    leftValues.sort()
    rightValues.sort()
    
    for i in range(lenA):
        while (index < lenA and leftValues[index] <= rightValues[i]):
            count += (index - i)
            index += 1

            if count > 10000000:
                return -1
    print(count)
    
solution([1, 5, 2, 1, 4, 0])