def fourSumCount(nums1, nums2, nums3, nums4):
    arrayList = sorted(nums1 + nums2 + nums3 + nums4)
    n = len(arrayList)
    target = 0
    distinct = []
    count = 0
    
    for i in range(n - 3):
        j = i + 1
        third = j + 1
        last = n - 1

        while third < last:
            total = arrayList[i] + arrayList[j] + arrayList[third] + arrayList[last]
            if total == target:
                distinct.append((arrayList[i], arrayList[j], arrayList[third], arrayList[last]))
                count += 1
                third += 1
                last -= 1
            elif total < target:
                third += 1
            else:
                last -= 1
    return count

print(fourSumCount([1, 2], [-2, 1], [-1, 2], [0, 2]))
print(fourSumCount([0], [0], [0], [0]))
print(fourSumCount([-1, -1],[-1, 1],[-1, 1],[1, -1]))
