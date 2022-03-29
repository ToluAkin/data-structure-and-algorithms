def longestPalindrome(s):
    longestStr = ""
    strLen = len(s)
    longestLen = 0

    for i in range(strLen):
        left, right = i, i

        while left >= 0 and right < strLen and s[left] == s[right]:
            if (right - left + 1) > longestLen:
                longestStr = s[left:right+1]
                longestLen = right - left + 1
            left -= 1
            right += 1
        
        left, right = i, i + 1
        while left >= 0 and right < strLen and s[left] == s[right]:
            if (right - left + 1) > longestLen:
                longestStr = s[left:right+1]
                longestLen = right - left + 1
            left -= 1
            right += 1

    return longestStr


print(longestPalindrome("babad"))
