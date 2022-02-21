def mergeSort(A):
    if len(A) <= 1:
        return A

    middleIndex = len(A) // 2
    leftValues = mergeSort(A[:middleIndex])
    rightValues = mergeSort(A[middleIndex:])
    sortedList = []
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(leftValues) and rightIndex < len(rightValues):
        if leftValues[leftIndex] < rightValues[rightIndex]:
            sortedList.append(leftValues[leftIndex])
            leftIndex += 1
        else:
            sortedList.append(rightValues[rightIndex])
            rightIndex += 1
    sortedList += leftValues[leftIndex:]
    sortedList += rightValues[rightIndex:]
    print(sortedList)
    return sortedList
mergeSort([2, 1, 1, 2, 3, 1])