def longestCommonPrefix(strs):
    currentString = min(strs, key=len)
    previousString = ''

    for index in range(len(currentString)):
        prefix = True
        for j in strs:
            if not j[index] == currentString[index]:
                prefix = False

        if prefix:        
            previousString += currentString[index]
        else:
            break
    return previousString
# print(longestCommonPrefix(["dog","racecar","car"]))
# print(longestCommonPrefix(["flower","flow","flowder", "float", "floss", "flight"]))
print(longestCommonPrefix(["", ""]))
