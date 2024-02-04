def isPalindrome(x):
    x = str(x)
    mid = len(x) // 2
    firstHalf = x[:mid]
    lastHalf = x[mid:][::-1]
    
    for i in range(len(firstHalf)):
        if (firstHalf[i] == lastHalf[i]):
            continue
        else:
            return False
    return True

# print (isPalindrome(121))
# print (isPalindrome(-121))
# print (isPalindrome(12))
print (isPalindrome(9))