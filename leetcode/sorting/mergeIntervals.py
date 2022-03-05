def merge(intervals):
    intervals.sort()
    mergeResult = [intervals[0]]

    for first, second in intervals[1:]:
        lastIntervalEnd = mergeResult[-1][1]

        if first <= lastIntervalEnd:
            mergeResult[-1][1] = max(second, lastIntervalEnd)
        else:
            mergeResult.append([first, second])
    return mergeResult

print(merge([[1, 3], [8, 10], [15, 18], [2, 6]]))
