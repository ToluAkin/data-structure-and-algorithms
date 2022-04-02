def lengthOfLongestSubstring(s):
    lenString = len(s)
    if lenString <= 1:
        return lenString
    
    longest = 0
    pointer = 0
    new_dict = {}

    for i in range(lenString):
        value = s[i]
        while value in new_dict:
            new_dict.pop(s[pointer])
            pointer += 1
        new_dict[value] = value
        longest = max(longest, i - pointer + 1)
    return longest


print(lengthOfLongestSubstring("dvdf"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("dvdfvmdf"))
print(lengthOfLongestSubstring("ohvhjdml"))
