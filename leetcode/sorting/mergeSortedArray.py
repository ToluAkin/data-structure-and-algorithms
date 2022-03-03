def merge(nums1, m , nums2, n):
    firstLength = len(nums1)
    secondLength = len(nums2)

    if firstLength == 1 and secondLength == 1:
        nums1[0] = nums2[0]
        return nums1
    
    if secondLength:
        i = m - 1
        j = n - 1
        l = (n + m) - 1

        while i > -1 and j > -1:
            if nums1[i] > nums2[j]:
                maxNum = nums1[i]
            else:
                maxNum = nums2[j]
            
            if maxNum == nums1[i]:
                i -= 1
            else:
                j -= 1
            
            nums1[l] = maxNum
            l -= 1

        if i == -1:
            while j > -1:
                nums1[j] = nums2[j]
                j -= 1
        return nums1   
# print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge([2, 0], 1, [1], 1))


