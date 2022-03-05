def swapMerge(mergeArray, newArray):
    if newArray[1] < mergeArray[-1][0] and newArray[1] < mergeArray[-1][1]:
        mergeArray.append(newArray)
        mergeArray[-1], mergeArray[-2] = mergeArray[-2], mergeArray[-1]
    elif newArray[0] <= mergeArray[-1][1]:
        if newArray[0] < mergeArray[-1][0]:
            mergeArray[-1][0] = newArray[0]
        mergeArray[-1][1] = max(newArray[1], mergeArray[-1][1])
    else:
        mergeArray.append(newArray)
    return mergeArray

def insert(intervals, newInterval):
    intervalLen = len(intervals)

    if intervalLen == 0:
        return [newInterval]
    elif intervalLen == 1:
        swapMerge(intervals, newInterval)

    mergeInsert = [intervals[0]]
    intervalBool = True
    for interval in intervals[1:]:
        if intervalBool:
            swapMerge(mergeInsert, newInterval)
            intervalBool = False

        swapMerge(mergeInsert, interval)
    return mergeInsert
    
print(insert([[1, 3], [6, 9]], [4, 5]))
print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(insert([[1, 5]], [2, 7]))
print(insert([[1, 5]], [6, 8]))
print(insert([[1, 5]], [0, 3]))
print(insert([[1, 5]], [0, 0]))
# https://leetcode.com/problems/insert-interval/