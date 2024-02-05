def firstUniqChar(s):
    characterDict = {}
    
    for i in range(len(s)):
        if s[i] in characterDict: # check if a key exist in a dictionary
            if characterDict[s[i]] == -1: # check if the value is -1
                continue
            else:
                characterDict[s[i]] = -1 # set value as -1 if it is repeating
        else:
            characterDict[s[i]] = i

    for char in characterDict:  # check the dictionary for the first unique character and return the position
        if characterDict[char] != -1:
            return characterDict[char]
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))
print(firstUniqChar("slow"))