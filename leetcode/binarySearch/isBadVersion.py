def firstBadVersion(n):
    if n == 1:
        return 1

    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2
        print(left, right, mid)
        if isBadVersion(mid) is True and isBadVersion(mid - 1) is False:
            return mid
        elif isBadVersion(mid) is False:
            left = mid + 1
        else:
            right = mid
    return -1
