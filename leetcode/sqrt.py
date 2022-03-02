def mySqrt(x):
    if x == 0:
        return 0
    elif x < 4:
        return 1
     
    left = 0
    right = x // 2

    while left <= right:
        mid = (left + right) // 2
        print(left, right, mid)

        if ((mid * mid) <= x) and ((mid + 1) * (mid + 1) > x):
            return mid
        elif x > (mid * mid):
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(mySqrt(2))
